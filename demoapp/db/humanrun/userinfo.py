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
根据手机号获取user_info信息
身份证、手机号、姓名
'''
def getUserInfo(mobile):
    # 查询user_info中的身份证
    id_number = UserInfo.objects.filter(username=mobile, user_type='LABOR').values('id_number')[0]['id_number']
    # 查询user_info中的姓名
    name = UserInfo.objects.filter(username=mobile, user_type='LABOR').values('real_name')[0]['real_name']
    params = {}
    params['mobile'] = mobile
    params['name'] = name
    params['id_number'] = id_number
    return params