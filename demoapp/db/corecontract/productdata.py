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
根据busrename获取销售合同产品信息：
1、产品id  2、任务类型  3、邀请码
'''
def getProductData(busrename):
    '''
    filter表示过滤条件，相当于where条件，可以传多个参数，相当于where后多个条件用and拼接
    exclude表示排除条件，即排除符合括号内符合条件的记录，[:1]即切片，表示取第一条
    order_by('-id')表示根据id倒序，order_by('id')表示升序
    '''

    '''
    下面查询B销售合同对应的product_id
    '''
    # 查询B登录账号的公司id
    b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    # 查询该B公司的销售合同
    sale_contract_id = \
    Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
                            status=0).order_by('-id')[:1].values('id')[0]['id']
    # 查询销售合同对应的非全承揽产品id
    sale_fc_product_data_id = \
    ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1).exclude(
        tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']
    # 查询销售合同对应的临时个体产品id
    sale_lg_product_data_id = \
    ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1,
                                tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']

    '''
    下面查询B公司支持的任务类型
    '''
    # 查询非全承揽任务支持的任务类型
    sale_fc_task_type = ProductData.objects.filter(id=sale_fc_product_data_id).values('sale_task_type')[0][
        'sale_task_type']
    # 任务类型字段存的格式为'1，4，7'，转成tuple返回
    sale_fc_task_type = eval(sale_fc_task_type)
    # 查询临时个体任务支持的任务类型
    sale_lg_task_type = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_task_type')[0][
        'sale_task_type']
    # 任务类型字段存的格式为'1，4，7'，转成tuple返回
    sale_lg_task_type = eval(sale_lg_task_type)

    '''
    下面查询B公司的邀请码
    '''
    invitation_code = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_invitation_code')[0][
        'sale_invitation_code']

    params = {}
    params['sale_fc_product_data_id'] = sale_fc_product_data_id
    params['sale_lg_product_data_id'] = sale_lg_product_data_id
    params['sale_fc_task_type'] = sale_fc_task_type
    params['sale_lg_task_type'] = sale_lg_task_type
    params['invitation_code'] = invitation_code
    return params