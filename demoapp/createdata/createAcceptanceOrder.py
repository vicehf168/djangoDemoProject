from demoapp.common.createcommondata import *

class CreateAcceptanceOrder():

    '''
    生成临时个体-B端待验收订单
    反向导入生成待验收任务（反向导入的模板excel文件在files目录下，根据传来的手机号获取用户信息，并修改至excel中）
    '''

    def createLgAcceptanceOrder(self,btoken,mobile,busername,tasknumber):
        returnParams = {}
        returnParams['responseCon'] = 'success'

        # 反向导入
        params = CreateCommonData().createLgPayOrder(btoken, mobile, busername, tasknumber)
        if params['responseCon'] != 'success':
            returnParams['responseCon'] = params['responseCon']
            return returnParams

        return returnParams