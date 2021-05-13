import json
import requests
import time,datetime
import random
import json,requests
from flaborapp.models import *
from eplatformapp.models import *
from corecontractapp.models import *
from humanrunapp.models import UserInfo

class FrontInit():


    '''
    获取B端登录token
    '''
    def b_login_token(self,username,password):
        url = 'https://egate-uat.renliwo.com/egate/eplatform/login'
        params = {}
        params['appId'] = 'eplatform'
        params['username'] = username
        params['password'] = password
        #请求参数json格式
        params_json = json.dumps(params)
        #post请求
        response_params = requests.post(url,params_json)
        #获取token
        token = response_params.headers['token']
        return token

    '''
    获取V端登录token
    '''
    def v_login_token(self, username, password):
        url = 'https://egate-uat.renliwo.com/egate/eplatform/loginVendor'
        params = {}
        params['appId'] = 'eplatform'
        params['username'] = username
        params['password'] = password
        # 请求参数json格式
        params_json = json.dumps(params)
        # post请求
        response_params = requests.post(url, params_json)
        # 获取token
        token = response_params.headers['token']
        return token