from demoapp.db.corecontract.productdata import *

class ForwardInviteTask():


    '''
    正向-非全-支付宝-邀请
    '''
    def fqAlipayInviteTask(self, btoken, busername, tasknumber, mobile):
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
        params['exhibitionType'] = 2     # 1:app  2:支付宝
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
        params['requireNum'] = 0
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向非全支付宝邀请' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = [{'name': 'invitename', 'mobile': mobile, 'reward': '11.11'}]
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 0
        params['taskType'] = 2     # 非全：2   承揽：1（invitation_code为空）   临时个体：1+邀请码（invitation_code非空）
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-非全-app-邀请
    '''
    def fqAppInviteTask(self, btoken, busername, tasknumber, mobile):
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
        params['requireNum'] = 0
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向非全app邀请' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = [{'name': 'invitename', 'mobile': mobile, 'reward': '11.11'}]
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 0
        params['taskType'] = 2
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-承揽-支付宝-邀请
    '''
    def clAlipayInviteTask(self, btoken, busername, tasknumber, mobile):
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
        params['requireNum'] = 0
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向承揽支付宝邀请' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = [{'name': 'invitename', 'mobile': mobile, 'reward': '11.11'}]
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 0
        params['taskType'] = 1
        params['workType'] = random.choice(product_data_params['sale_fc_task_type'])

        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)

    '''
    正向-承揽-app-邀请
    '''
    def clAppInviteTask(self, btoken, busername, tasknumber, mobile):
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
        params['requireNum'] = 0
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向承揽app邀请' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = [{'name': 'invitename', 'mobile': mobile, 'reward': '11.11'}]
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
    正向-临时个体-支付宝-邀请
    '''
    def lgAlipayInviteTask(self, btoken, busername, tasknumber, mobile):
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
        params['productDataId'] = product_data_params['sale_fc_product_data_id']
        params['provinceCode'] = 29
        params['requireNum'] = 0
        params['settlementMaterial'] = ''
        params['settlementRules'] = '任务规则任务规则任务规则任务规则任务规则任务规则'
        params['sex'] = 2
        params['startTime'] = currentTime  # 开始时间定义当前时间
        params['submitForm'] = '2'
        params['taskDesc'] = '任务描述任务描述任务描述任务描述任务描述任务描述'
        taskName = '正向临时个体支付宝邀请' + tasknumber
        params['taskName'] = taskName
        params['taskOrderList'] = [{'name': 'invitename', 'mobile': mobile, 'reward': '11.11'}]
        params['taskPunchPosition'] = 'renliwo'
        params['taskReward'] = 0
        params['taskType'] = 1
        params['workType'] = random.choice(product_data_params['sale_lg_task_type'])
        # json组装请求参数
        params_json = json.dumps(params)
        header = {}
        header['content-type'] = 'application/json'
        header['token'] = btoken
        response_params = requests.post(url, data=params_json, headers=header)