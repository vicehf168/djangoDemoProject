import xlrd
from demoapp.common.desCon import *
from xlutils import copy
from requests_toolbelt import MultipartEncoder
from demoapp.common.frontinit import *
from demoapp.db.corebill.invoiceorder import *
from demoapp.db.corebill.orderinfo import *
from demoapp.db.corebill.transactionbankinfo import *
from demoapp.db.corebill.confirmpaymentsetting import *
from demoapp.db.corecontract.invoice import *
from demoapp.db.corecontract.productdata import *
from demoapp.db.eplatform.tcorpaccount import *
from demoapp.db.eplatform.tcorpuser import *
from demoapp.db.flabor.flaborsettlementwork import *
from demoapp.db.flabor.taskorder import *
from demoapp.db.humanrun.userinfo import *

class CreateCommonData():


    '''
    生成临时个体-B端待结算订单
    步骤：1、反向导入生成待验收任务（反向导入的模板excel文件在files目录下，根据传来的手机号获取用户信息，并修改至excel中）
    2、验收生成待结算订单
    '''
    def createLgPayOrder(self, btoken, mobile, busername, tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/settlement/importExcel'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')

        params = {}
        taskName = '临时个体结算' + tasknumber
        params['taskName'] = taskName
        # 查询获取的任务类型为tuple，随机取其中一个
        params['workType'] = str(random.choice(product_data_params['sale_lg_task_type']))
        params['startTime'] = currentTime
        params['endTime'] = nextTime
        params['isLine'] = '1'
        params['provinceCode'] = '-1'
        params['cityCode'] = '-2'
        params['areaCode'] = '-3'
        params['address'] = '全国（港澳台除外)'
        params['taskDesc'] = '任务描述'
        params['settlementRules'] = '任务规则'
        params['issueAttribute'] = '1'  # 1-应发/含税      2-实发/不含税
        params['productDataId'] = str(product_data_params['sale_lg_product_data_id'])

        # 获取userinfo信息
        userInfo = getUserInfo(mobile)

        # 修改反向导入模板excel的数据，使之填写前台传来的手机号在user_info中对应的数据：身份证、姓名、手机号，从而反向导入
        self.modifyExcelData(userInfo['mobile'], userInfo['name'], userInfo['id_number'])
        # 不建议下面这种传值方式，因为getUserInfo方法的返回参数个数可能会变
        # self.modifyExcelData(**(getUserInfo(mobile)))

        # 1、参数加rb，是以二进制的方法读取（encoding不管是用utf8、gb2312、gbk编码方式都不行的前提下）
        # 2、multipart/form-data格式请求，当参数包括文件时，固定用下面的方式传参
        params['multipartfiles'] = (
            '结算订单导入模板.xls', open('demoapp/files/结算订单导入模板.xls', 'rb'), 'application/octet-stream')

        # 参数组装好之后，转成multipart/form-data格式
        params_formdata = MultipartEncoder(params)
        header = {}
        header['token'] = btoken
        # 设置Content-Type为请求参数为转换成multipart/form-data之后的类型，否则后端接收判定不是form/data格式
        header['Content-Type'] = params_formdata.content_type
        response_params = requests.post(url, data=params_formdata, headers=header)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] = '反向导入接口： ' + responseMsg
            return returnParams
        print('反向导入接口:       ',response_params.text)

        '''
        返回参数，用以后面的接口
        '''
        # 以下要在大V、小V端操作，因此先获取大V、小V token
        # 获取大V用户名
        dvUserName = getVUserNameByBUserName(busername)['dvUserName']
        # 获取小V用户名
        xvUserName = getVUserNameByBUserName(busername)['xvUserName']
        # 获取大V token
        dvToken = FrontInit().v_login_token(dvUserName, '12345678')
        # 获取小V token
        xvToken = FrontInit().v_login_token(xvUserName, '12345678')
        # 判断大V是否自动审核
        dvAllowAutoConfirm = getVAllowAutoConfirm(dvUserName)['v_AllowAutoConfirm']
        # 判断小V是否自动审核
        xvAllowAutoConfirm = getVAllowAutoConfirm(xvUserName)['v_AllowAutoConfirm']


        returnParams['btoken'] = btoken
        returnParams['taskname'] = params['taskName']
        returnParams['mobile'] = mobile
        returnParams['name'] = userInfo['name']
        returnParams['busername'] = busername
        returnParams['taskTypeId'] = params['workType']
        returnParams['dvUserName'] = dvUserName
        returnParams['dvToken'] = dvToken
        returnParams['xvToken'] = xvToken
        returnParams['dvAllowAutoConfirm'] = dvAllowAutoConfirm
        returnParams['xvAllowAutoConfirm'] = xvAllowAutoConfirm
        # bUserName, dvToken, taskName
        return returnParams



    '''
    修改结算导入模板数据
    '''
    def modifyExcelData(self, mobile, name, id_number):
        # 关于文件路径的问题需要深入研究，很多时候文件的相对路径，并非相对于当前所执行的py脚本的路径
        book = xlrd.open_workbook('demoapp/files/结算订单导入模板.xls')
        # sheet = book.sheet_by_index(0)
        # print(sheet.nrows, sheet.ncols)

        new_book = copy.copy(book)
        new_sheet = new_book.get_sheet(0)
        new_sheet.write(1, 0, mobile)
        new_sheet.write(1, 1, name)
        new_sheet.write(1, 2, id_number)
        new_sheet.write(1, 3, '22')
        new_book.save('demoapp/files/结算订单导入模板.xls')


    '''
    验收（反向导入待验收的任务）
    '''
    def acceptance(self, btoken, taskname, mobile, name):
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/order/taskCheckBeforeAcceptance'
        params = {}
        params['acceptanceResult'] = 1
        params['appId'] = 'eplatform'
        task_order_id = getTaskOrder(taskname)['task_order_id']
        params['id'] = desCrypt().desEncrypt(str(task_order_id))
        params['mobile'] = mobile
        params['name'] = name

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = btoken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('B验收接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='B验收接口： ' +  responseMsg
        return returnParams



    '''
    B端结算
    '''
    def bSettlement(self, btoken, busername, taskName, taskTypeId):
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/settlement/applyWorkList'
        # 获取开票信息
        invoiceData = getInvoice(busername)
        params = {}
        params['appId'] = 'eplatform'
        params['remark'] = ''
        params['smsSwitch'] = 'false'
        params['workBatchInvoiceDtoList'] = []
        invoiceParams = {}
        invoiceParams['invoiceCategory'] = random.choice(invoiceData['invoice_category'])
        invoiceParams['invoiceContent'] = invoiceData['invoice_content']
        invoiceParams['invoiceOrderNumber'] = ''
        invoiceParams['invoiceType'] = random.choice(invoiceData['invoice_type'])
        invoiceParams['preInvoiceOrder'] = '2'
        invoiceParams['taskName'] = taskName
        invoiceParams['taskTypeId'] = desCrypt().desEncrypt(str(taskTypeId))  # 任务类型id
        params['workBatchInvoiceDtoList'].append(invoiceParams)
        params['workIdList'] = []
        params['workIdList'].append(
            desCrypt().desEncrypt(str(getFlaborSettlementWork(taskName)['workId'])))  # work表的workid，而非id

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = btoken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('B结算接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='B申请结算接口： ' +  responseMsg
        return returnParams



    '''
    大V端审核成功
    '''
    def dvReview(self, bUserName, dvToken, taskName):
        url = 'https://egate-uat.renliwo.com/egate/flabor/bill/orderInfo/reviewOrderInfo'
        orderInfo = getOrderInfo(taskName)
        corpBalance = getCorpAmount(bUserName)  # 公司账户余额
        params = {}
        params['appId'] = 'eplatform'
        # confirmAmount=销售订单订单支付总金额-当前B用户灵工账户余额
        params['confirmAmount'] = str(orderInfo['saleTotalAmount'] - corpBalance['flaborBalance'])
        params['confirmFormList'] = []
        params['orderInfoId'] = desCrypt().desEncrypt(str(orderInfo['saleOrderInfoId']))
        params['orderNumberList'] = []
        # orderinfo中销售订单对应的开票订单invoice_order中的order_number
        orderNumber = getInvoiceOrder(taskName)['sale_order_number']
        params['orderNumberList'].append(orderNumber)
        params['reviewStatus'] = 2
        params['reviseAmount'] = 0
        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = dvToken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('大V审核接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='大V审核成功接口： ' +  responseMsg
        return returnParams



    '''
    支付前先发短信验证码
    '''
    def paySmsApply(self, dvToken, taskName):
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/settlement/applySmsCodeSend'
        params = {}
        params['appId'] = 'eplatform'
        params['orderNumberList'] = []
        # orderinfo中采购订单对应的开票订单invoice_order中的order_number
        orderNumber = getInvoiceOrder(taskName)['buy_order_number']
        params['orderNumberList'].append(orderNumber)

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = dvToken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('大V支付前发短信接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='大V支付发短信接口： ' +  responseMsg
            return returnParams
        bizNo = response_params.json()['result']['bizNo']
        returnParams['bizNo'] = bizNo
        return returnParams

        # response_params.json()直接返回一个dict，而response_params.text返回的是str需要再转换



    '''
    大V支付
    '''
    def dvPayApply(self, taskName, busername, dvToken, bizNo):
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/settlement/applyPay'
        params = {}
        params['appId'] = 'eplatform'
        params['bizNo'] = bizNo
        params['channel'] = 'mybank'
        params['orderNumberList'] = []
        # orderinfo中采购订单对应的开票订单invoice_order中的order_number
        orderNumber = getInvoiceOrder(taskName)['buy_order_number']
        params['orderNumberList'].append(orderNumber)
        params['password'] = ''
        # orderinfo采购订单的付款方公司名
        params['payFromAccount'] = getOrderInfo(taskName)['buyOrderPayerCorpName']
        params['payFromBankNo'] = getOrderInfo(taskName)['buyOrderPayerBankNumber']
        params['payFromMobile'] = getTransactionBankInfo(busername, params['payFromBankNo'])['payerMobile']
        params['payRemark'] = ''
        params['payTargetAccount'] = getOrderInfo(taskName)['buyOrderPayeeCorpName']
        params['payTargetBankNo'] = getOrderInfo(taskName)['buyOrderPayeeBankNumber']
        params['smsCode'] = '1'

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = dvToken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('大V支付接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='大V支付接口： ' +  responseMsg
        return returnParams


    '''
    小V端审核成功
    '''
    def xvReview(self, dvUserName, xvToken, taskName):
        url = 'https://egate-uat.renliwo.com/egate/flabor/bill/orderInfo/reviewOrderInfo'
        orderInfo = getOrderInfo(taskName)
        corpBalance = getCorpAmount(dvUserName)  # 公司账户余额
        params = {}
        params['appId'] = 'eplatform'
        # confirmAmount=销售订单订单支付总金额-当前大V用户灵工账户余额
        params['confirmAmount'] = str(orderInfo['buyTotalAmount'] - corpBalance['flaborBalance'])
        params['confirmFormList'] = []
        params['orderInfoId'] = desCrypt().desEncrypt(str(orderInfo['buyOrderInfoId']))
        params['orderNumberList'] = []
        # orderinfo中采购订单对应的开票订单invoice_order中的order_number
        orderNumber = getInvoiceOrder(taskName)['buy_order_number']
        params['orderNumberList'].append(orderNumber)
        params['reviewStatus'] = 2
        params['reviseAmount'] = 0
        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['token'] = xvToken
        header['content-type'] = 'application/json'
        response_params = requests.post(url, data=params_json, headers=header)
        print('小V审核接口:       ', response_params.text)
        returnParams = {}
        returnParams['responseCon'] = 'success'
        responseCode = response_params.json()['code']
        responseMsg = response_params.json()['msg']
        if not responseCode or responseCode != '200' or responseMsg != '':
            returnParams['responseCon'] ='小V审核成功接口： ' +  responseMsg
        return returnParams
