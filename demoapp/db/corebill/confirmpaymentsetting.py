from corebillapp.models import *
from eplatformapp.models import *

def getVAllowAutoConfirm(username):
    # 查询V登录账号的公司id
    v_corpid = TCorpUser.objects.filter(username=username).values('corp_id')[0]['corp_id']
    v_AllowAutoConfirm = ConfirmPaymentSetting.objects.filter(payee_corp_id=v_corpid,task_type=3,is_delete=0)
    if v_AllowAutoConfirm:        # 判断v_AllowAutoConfirm存在，既非None，也非空对象（任何类型的空对象）
        v_AllowAutoConfirm = v_AllowAutoConfirm.values('allow_auto_confirm')[0]['allow_auto_confirm']
    params = {}
    params['v_AllowAutoConfirm'] = v_AllowAutoConfirm
    return params