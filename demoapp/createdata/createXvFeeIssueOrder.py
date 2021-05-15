from demoapp.common.createcommondata import *

class CreateXvFeeIssueOrder():

    '''
    小V审核成功，生成小V待费用发放订单
    '''
    def createXvLgFeeIssueOrder(self, btoken, mobile, busername, tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'

        # 反向导入
        params = CreateCommonData().createLgPayOrder(btoken, mobile, busername, tasknumber)
        if params['responseCon'] != 'success':
            returnParams['responseCon'] = params['responseCon']
            return returnParams

        '''
        获取以下接口所需的参数
        '''
        btoken = params['btoken']
        taskName = params['taskname']
        mobile = params['mobile']
        name = params['name']
        bUserName = params['busername']
        taskTypeId = params['taskTypeId']
        dvUserName = params['dvUserName']
        dvToken = params['dvToken']
        xvToken = params['xvToken']
        dvAllowAutoConfirm = params['dvAllowAutoConfirm']
        xvAllowAutoConfirm = params['xvAllowAutoConfirm']

        # 验收（反向导入待验收的任务）
        acceptance = CreateCommonData().acceptance(btoken, taskName, mobile, name)
        if acceptance['responseCon'] != 'success':
            returnParams['responseCon'] = acceptance['responseCon']
            return returnParams

        # B端申请结算
        bSettlement = CreateCommonData().bSettlement(btoken, bUserName, taskName, taskTypeId)
        if bSettlement['responseCon'] != 'success':
            returnParams['responseCon'] = bSettlement['responseCon']
            return returnParams

        # 大V审核成功，需判断是否自动审核
        if dvAllowAutoConfirm and dvAllowAutoConfirm == 1:
            pass       # 什么都不做，但是会继续执行if else下面的代码
        else:
            dvReview = CreateCommonData().dvReview(bUserName, dvToken, taskName)
            if dvReview['responseCon'] != 'success':
                returnParams['responseCon'] = dvReview['responseCon']
                return returnParams

        # 大V支付前置-发短信验证码
        paySmsApply = CreateCommonData().paySmsApply(dvToken, taskName)
        if paySmsApply['responseCon'] != 'success':
            returnParams['responseCon'] = paySmsApply['responseCon']
            return returnParams

        # 大V支付成功
        dvPayApply = CreateCommonData().dvPayApply(taskName, busername, dvToken, paySmsApply['bizNo'])
        if dvPayApply['responseCon'] != 'success':
            returnParams['responseCon'] = dvPayApply['responseCon']
            return returnParams

        # 小V审核成功，需判断是否自动审核
        if xvAllowAutoConfirm and xvAllowAutoConfirm == 1:
            pass
        else:
            xvReview = CreateCommonData().xvReview(dvUserName, xvToken, taskName)
            if xvReview['responseCon'] != 'success':
                returnParams['responseCon'] = xvReview['responseCon']
                return returnParams

        return returnParams

