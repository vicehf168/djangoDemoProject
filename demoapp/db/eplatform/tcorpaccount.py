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
查询公司账户余额信息
'''
def getCorpAmount(corpUserName):
    # 获取企业id
    corpId = TCorpUser.objects.filter(username=corpUserName).values('corp_id')[0]['corp_id']
    # 获取公司灵工账户余额
    flaborBalance = TCorpAccount.objects.filter(corp_id=corpId).values('task_amount')[0]['task_amount']
    params = {}
    params['flaborBalance'] = flaborBalance
    return params