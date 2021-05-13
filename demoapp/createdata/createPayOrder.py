from demoapp.common.createcommondata import *

class CreatePayOrder():

    '''
    大V审核成功，生成大V待支付订单
    '''
    def createLgPayOrder(self,btoken,mobile,busername,tasknumber):
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
        dvToken = params['dvToken']
        dvAllowAutoConfirm = params['dvAllowAutoConfirm']

        # 验收（反向导入待验收的任务）
        CreateCommonData().acceptance(btoken, taskName, mobile, name)
        # B端申请结算
        CreateCommonData().bSettlement(btoken, bUserName, taskName, taskTypeId)
        if dvAllowAutoConfirm and dvAllowAutoConfirm == 1:
            pass
        else:
            # 大V审核成功
            CreateCommonData().dvReview(bUserName, dvToken, taskName)