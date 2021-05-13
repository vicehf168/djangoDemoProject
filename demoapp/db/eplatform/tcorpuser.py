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
查询B端所有用户名
'''
def getAllBUserName():
    allUserName = list(TCorpUser.objects.all().values('username'))
    return allUserName


'''
根据B端用户名查询大V用户名（主账号）
'''
def getVUserNameByBUserName(busername):
    # 查询B登录账号的公司id
    b_corpid = TCorpUser.objects.filter(username=busername).values('corp_id')[0]['corp_id']
    # 查询该B公司在销售合同中对应的大V公司id
    dvCorpId = \
        Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
                                    status=0).order_by('-id')[:1].values('party_b_corp_id')[0]['party_b_corp_id']
    # 查询该B公司对应的销售合同id
    contractId = \
        Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
                                status=0).order_by('-id')[:1].values('id')[0]['id']
    # 查询该销售合同对应的productdata中的sale_vendor（指定供应商）
    xvCorpId = ProductData.objects.filter(contract_id=contractId,biz_category='flabor',status=1,is_delete=0).order_by('-id')[:1].values('sale_vendor')[0]['sale_vendor']
    # 根据公司id去t_corp_user查询大V公司下的主账号
    dvUserName = TCorpUser.objects.filter(corp_id=dvCorpId, level=1, is_delete=0).order_by('-id')[:1].values('username')[0]['username']
    # 根据公司id去t_corp_user查询小V公司下的主账号
    xvUserName = \
    TCorpUser.objects.filter(corp_id=xvCorpId, level=1, is_delete=0).order_by('-id')[:1].values('username')[0][
        'username']
    params = {}
    params['dvUserName'] = dvUserName
    params['xvUserName'] = xvUserName
    return params