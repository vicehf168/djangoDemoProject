from demoapp.common.createcommondata import *

class CreateXvFeeIssueOrder():
    '''
    小V审核成功，生成小V待费用发放订单
    '''
    def createXvLgFeeIssueOrder(self, btoken, mobile, busername, tasknumber):
        # 反向导入
        params = CreateCommonData().createLgPayOrder(btoken, mobile, busername, tasknumber)
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
        CreateCommonData().acceptance(btoken, taskName, mobile, name)
        # B端申请结算
        CreateCommonData().bSettlement(btoken, bUserName, taskName, taskTypeId)
        # 大V审核成功，需判断是否自动审核
        if dvAllowAutoConfirm and dvAllowAutoConfirm == 1:
            pass       # 什么都不做，但是会继续执行if else下面的代码
        else:
            CreateCommonData().dvReview(bUserName, dvToken, taskName)
        # 大V支付前置-发短信验证码
        bizNo = CreateCommonData().paySmsApply(dvToken, taskName)
        # 大V支付成功
        CreateCommonData().dvPayApply(taskName, busername, dvToken, bizNo)
        # 小V审核成功，需判断是否自动审核
        if xvAllowAutoConfirm and xvAllowAutoConfirm == 1:
            pass
        else:
            CreateCommonData().xvReview(dvUserName, xvToken, taskName)

