from demoapp.common.createcommondata import *

class CreateReviewOrder():

    '''
    生成临时个体-B端待结算订单
    步骤：1、反向导入生成待验收任务（反向导入的模板excel文件在files目录下，根据传来的手机号获取用户信息，并修改至excel中）
         2、验收生成待结算订单
    '''
    def createLgReviewOrder(self,btoken,mobile,busername,tasknumber):
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

        # 验收（反向导入待验收的任务）
        CreateCommonData().acceptance(btoken, taskName, mobile, name)
        # B端申请结算
        CreateCommonData().bSettlement(btoken, bUserName, taskName, taskTypeId)