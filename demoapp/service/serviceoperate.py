from demoapp.db.eplatform.tcorpuser import *
from demoapp.service.serviceoperate import *
from demoapp.createdata.forwardPublicTask import *
from demoapp.createdata.forwardInviteTask import *
from demoapp.createdata.createSettlementOrder import *
from demoapp.createdata.createAcceptanceOrder import *
from demoapp.createdata.createReviewOrder import *
from demoapp.createdata.createPayOrder import *
from demoapp.createdata.createXvReviewOrder import *
from demoapp.createdata.createXvFeeIssueOrder import *

class ServiceOperate():

    '''
    正向公开抢单任务
    '''
    def forwardPublicTaskService(self,b_token, public_TaskType, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'

        # 生成正向公开任务
        if public_TaskType == 'fqAlipayPublicTask':  # 非全-支付宝-抢单
            publicTask = ForwardPublishTask().fqAlipayPublicTask(b_token, username, tasknumber)
            if publicTask['responseCon'] != 'success':
                returnParams['responseCon'] = publicTask['responseCon']
        elif public_TaskType == 'fqAppPublicTask':  # 非全-app-抢单
            publicTask = ForwardPublishTask().fqAppPublicTask(b_token, username, tasknumber)
            if publicTask['responseCon'] != 'success':
                returnParams['responseCon'] = publicTask['responseCon']
        elif public_TaskType == 'clAlipayPublicTask':  # 承揽-支付宝-抢单
            publicTask = ForwardPublishTask().clAlipayPublicTask(b_token, username, tasknumber)
            if publicTask['responseCon'] != 'success':
                returnParams['responseCon'] = publicTask['responseCon']
        elif public_TaskType == 'clAppPublicTask':  # 承揽-app-抢单
            publicTask = ForwardPublishTask().clAppPublicTask(b_token, username, tasknumber)
            if publicTask['responseCon'] != 'success':
                returnParams['responseCon'] = publicTask['responseCon']
        elif public_TaskType == 'lgAlipayPublicTask':  # 临时个体-支付宝-抢单
            publicTask = ForwardPublishTask().lgAlipayPublicTask(b_token, username, tasknumber)
            if publicTask['responseCon'] != 'success':
                returnParams['responseCon'] = publicTask['responseCon']

        return returnParams


    '''
    正向邀请任务
    '''
    def forwardInviteTaskService(self, b_token, invite_TaskType, username, tasknumber, mobile):
        returnParams = {}
        returnParams['responseCon'] = 'success'

        # 生成正向邀请任务
        if invite_TaskType == 'fqAlipayInviteTask':  # 非全-支付宝-邀请
            inviteTask = ForwardInviteTask().fqAlipayInviteTask(b_token, username, tasknumber, mobile)
            if inviteTask['responseCon'] != 'success':
                returnParams['responseCon'] = inviteTask['responseCon']
        elif invite_TaskType == 'fqAppInviteTask':  # 非全-app-邀请
            inviteTask = ForwardInviteTask().fqAppInviteTask(b_token, username, tasknumber, mobile)
            if inviteTask['responseCon'] != 'success':
                returnParams['responseCon'] = inviteTask['responseCon']
        elif invite_TaskType == 'clAlipayInviteTask':  # 承揽-支付宝-邀请
            inviteTask = ForwardInviteTask().clAlipayInviteTask(b_token, username, tasknumber, mobile)
            if inviteTask['responseCon'] != 'success':
                returnParams['responseCon'] = inviteTask['responseCon']
        elif invite_TaskType == 'clAppInviteTask':  # 承揽-app-邀请
            inviteTask = ForwardInviteTask().clAppInviteTask(b_token, username, tasknumber, mobile)
            if inviteTask['responseCon'] != 'success':
                returnParams['responseCon'] = inviteTask['responseCon']
        elif invite_TaskType == 'lgAlipayInviteTask':  # 临时个体-支付宝-邀请
            inviteTask = ForwardInviteTask().lgAlipayInviteTask(b_token, username, tasknumber, mobile)
            if inviteTask['responseCon'] != 'success':
                returnParams['responseCon'] = inviteTask['responseCon']

        return returnParams


    '''
    生成B端待结算订单
    '''
    def createSettlementOrderService(self, b_token, settlementType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if settlementType == 'lgSettlement':  # 临时个体验收任务
            CreateLgSettlementOrder = CreateSettlementOrder().CreateLgSettlementOrder(b_token, mobile, username, tasknumber)
            if CreateLgSettlementOrder['responseCon'] != 'success':
                returnParams['responseCon'] = CreateLgSettlementOrder['responseCon']
        return returnParams

    '''
    生成B端待验收订单
    '''
    def createAcceptanceOrderService(self, b_token, acceptanceType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if acceptanceType == 'lgAcceptance':  # 临时个体验收任务
            createLgAcceptanceOrder = CreateAcceptanceOrder().createLgAcceptanceOrder(b_token, mobile, username, tasknumber)
            if createLgAcceptanceOrder['responseCon'] != 'success':
                returnParams['responseCon'] = createLgAcceptanceOrder['responseCon']
        return returnParams

    '''
    生成大V端待审核订单
    '''
    def createReviewOrderService(self, b_token, reviewType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if reviewType == 'lgReview':  # 临时个体验收任务
            createLgReviewOrder = CreateReviewOrder().createLgReviewOrder(b_token, mobile, username, tasknumber)
            if createLgReviewOrder['responseCon'] != 'success':
                returnParams['responseCon'] = createLgReviewOrder['responseCon']
        return returnParams

    '''
    生成大V端待支付订单
    '''
    def createPayOrderService(self, b_token, payType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if payType == 'lgPay':  # 临时个体验收任务
            createLgPayOrder = CreatePayOrder().createLgPayOrder(b_token, mobile, username, tasknumber)
            if createLgPayOrder['responseCon'] != 'success':
                returnParams['responseCon'] = createLgPayOrder['responseCon']
        return returnParams

    '''
    生成小V端待审核订单
    '''
    def createXvReviewOrderService(self, b_token, xvReviewType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if xvReviewType == 'lgReview':  # 临时个体验收任务
            createXvLgReviewOrder = CreateXvReviewOrder().createXvLgReviewOrder(b_token, mobile, username, tasknumber)
            if createXvLgReviewOrder['responseCon'] != 'success':
                returnParams['responseCon'] = createXvLgReviewOrder['responseCon']
        return returnParams

    '''
    生成小V端待费用发放订单
    '''
    def createXvFeeIssueOrderService(self, b_token, xvFeeIssuType, mobile, username, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'
        if xvFeeIssuType == 'lgFeeIssueType':  # 临时个体验收任务
            createXvLgFeeIssueOrder = CreateXvFeeIssueOrder().createXvLgFeeIssueOrder(b_token, mobile, username, tasknumber)
            if createXvLgFeeIssueOrder['responseCon'] != 'success':
                returnParams['responseCon'] = createXvLgFeeIssueOrder['responseCon']
        return returnParams


    '''
    初始化所有B端用户名
    '''
    def queryUserNameService(self):
        allUserName = getAllBUserName()
        # 下面是超简便的方法：一个list中取出所有dict的value，比如list=[{'name':'fei','sex':'nan'},{'name':'hf'}]，取出来的是['fei','nan','hf']
        userNames = [item[key] for item in allUserName for key in item]
        params = []
        for userName in userNames:
            param = {}
            param['value'] = userName
            params.append(param)
        return params