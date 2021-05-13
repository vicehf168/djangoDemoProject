from demoapp.db.corecontract.productdata import *

class ForwardPublishTask():


    '''
    正向-非全-支付宝-公开抢单
    '''
    def fqAlipayPublicTask(self,btoken,busername,tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/publishTask'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')
        # 定义任务名称随机编号，用于数据校验，根据随机编号检索
        # randomTaskNo = ''
        # for f in range(10):
        #     a = random.randint(0, 9)
        #     randomTaskNo += str(a)

        params = {}
        params['address'] = '中央公园'
        params['appId'] = 'eplatform'
        params['areaCode'] = 3065
        params['cityCode'] = 360
        params['degree'] = 1
        params['endTime'] = nextTime  # 结束时间定义成当前时间后一天
        params['exhibitionType'] = 2
        params['experience'] = 1
        params['grabSheetAudit'] = 0
        params['isLine'] = 0
        params['latitude'] = 31.231706
        params['longitude'] = 121.472644
        params['needEndPunch'] = 0
        params['needMaterial'] = 0
        params['otherWorkTypeName'] = ''
        params['productDataId'] = product_data_params['sale_fc_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 5
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向非全支付宝公开' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = []
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 1.1
        params['taskType'] = 2
        # 任务类型为tuple类型，随机取其中一个
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-非全-app-公开抢单
    '''
    def fqAppPublicTask(self,btoken,busername,tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/publishTask'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')

        params = {}
        params['address'] = '中央公园'
        params['appId'] = 'eplatform'
        params['areaCode'] = 3065
        params['cityCode'] = 360
        params['degree'] = 1
        params['endTime'] = nextTime  # 结束时间定义成当前时间后一天
        params['exhibitionType'] = 1
        params['experience'] = 1
        params['grabSheetAudit'] = 0
        params['isLine'] = 0
        params['latitude'] = 31.231706
        params['longitude'] = 121.472644
        params['needEndPunch'] = 0
        params['needMaterial'] = 0
        params['otherWorkTypeName'] = ''
        params['productDataId'] = product_data_params['sale_fc_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 5
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向非全app公开' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = []
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 1.1
        params['taskType'] = 2
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-承揽-支付宝-公开抢单
    '''
    def clAlipayPublicTask(self,btoken,busername,tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/publishTask'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')

        params = {}
        params['address'] = '中央公园'
        params['appId'] = 'eplatform'
        params['areaCode'] = 3065
        params['cityCode'] = 360
        params['degree'] = 1
        params['endTime'] = nextTime  # 结束时间定义成当前时间后一天
        params['exhibitionType'] = 2
        params['experience'] = 1
        params['grabSheetAudit'] = 0
        params['invitationCode'] = ''
        params['isLine'] = 0
        params['latitude'] = 31.231706
        params['longitude'] = 121.472644
        params['needEndPunch'] = 0
        params['needMaterial'] = 0
        params['otherWorkTypeName'] = ''
        params['productDataId'] = product_data_params['sale_fc_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 5
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向承揽支付宝公开' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = []
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 1.1
        params['taskType'] = 1
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-承揽-app-公开抢单
    '''
    def clAppPublicTask(self,btoken,busername,tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/publishTask'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')

        params = {}
        params['address'] = '中央公园'
        params['appId'] = 'eplatform'
        params['areaCode'] = 3065
        params['cityCode'] = 360
        params['degree'] = 1
        params['endTime'] = nextTime  # 结束时间定义成当前时间后一天
        params['exhibitionType'] = 1
        params['experience'] = 1
        params['grabSheetAudit'] = 0
        params['invitationCode'] = ''
        params['isLine'] = 0
        params['latitude'] = 31.231706
        params['longitude'] = 121.472644
        params['needEndPunch'] = 0
        params['needMaterial'] = 0
        params['otherWorkTypeName'] = ''
        params['productDataId'] = product_data_params['sale_fc_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 5
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向承揽app公开' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = []
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 1.1
        params['taskType'] = 1
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-临时个体-支付宝-公开抢单
    '''
    def lgAlipayPublicTask(self, btoken, busername, tasknumber):
        product_data_params = getProductData(busername)
        url = 'https://egate-uat.renliwo.com/egate/flabor/task/publishTask'
        # 定义当前时间
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 获取当前时间后一天
        nextTime = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime('%Y-%m-%d %H:%M:%S')

        params = {}
        params['address'] = '中央公园'
        params['appId'] = 'eplatform'
        params['areaCode'] = 3065
        params['cityCode'] = 360
        params['degree'] = 1
        params['endTime'] = nextTime  # 结束时间定义成当前时间后一天
        params['exhibitionType'] = 2
        params['experience'] = 1
        params['grabSheetAudit'] = 0
        params['invitationCode'] = product_data_params['invitation_code']
        params['isLine'] = 0
        params['latitude'] = 31.231706
        params['longitude'] = 121.472644
        params['needEndPunch'] = 0
        params['needMaterial'] = 0
        params['otherWorkTypeName'] = ''
        params['productDataId'] = product_data_params['sale_lg_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 5
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向临时个体支付宝公开' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = []
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 1.1
        params['taskType'] = 1
        params['workType'] = random.choice(product_data_params['sale_lg_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)