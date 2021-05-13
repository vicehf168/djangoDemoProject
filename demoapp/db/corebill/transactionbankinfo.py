import json
import requests
import time,datetime
import random
import json,requests
from flaborapp.models import *
from eplatformapp.models import *
from corecontractapp.models import *
from humanrunapp.models import UserInfo
from corebillapp.models import *

'''
根据B端用户名查询大V在transaction_bank_info中的信息
'''
def getTransactionBankInfo(busrename, dvBankNumber):
    # 查询B登录账号的公司id
    b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    # 查询该B公司在销售合同中对应的大V公司id
    dvCorpId = \
        Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
                                status=0).order_by('-id')[:1].values('party_b_corp_id')[0]['party_b_corp_id']
    # 查询大V在transaction_bank_info中配的手机号，存在config_data字段中
    # config_data需根据卡号和corpid共同确定，因为transaction_bank_info中，一个corpid可以配多个卡号，因为可以有多个支付渠道：mybank、merchantsbank
    config_data = TransactionBankInfo.objects.filter(corporation_id=dvCorpId, bank_card_number=dvBankNumber, is_delete=0).order_by('-id')[:1].values('config_data')[0]['config_data']
    payerMobile = eval(config_data)['mobile']
    params = {}
    params['payerMobile'] = payerMobile
    return params