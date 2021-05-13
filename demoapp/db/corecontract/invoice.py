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
根据busrename获取B结算时所需的开票信息
开票模式、发票类型、开票内容
'''
def getInvoice(busrename):
    '''
    开票信息存在invoice表，因此先获取销售合同id，再根据合同id去invoice表查
    注：1、虽然invoice表存了开票模式、发票类型、开票内容，但是只有开票模式、发票类型在invoice表获取，
    开票内容的实际逻辑则要通过task_type_invoice_content、task_type_setting、invoice_content三者关联查找
    '''

    '''
    下面根据销售合同id，获取开票模式、发票类型
    '''
    # 查询B登录账号的公司id
    b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    # 查询该B公司的销售合同
    sale_contract_id = \
        Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
                                status=0).order_by('-id')[:1].values('id')[0]['id']
    # 查询在销售合同在incoice表中的开票模式、发票类型
    # 开票模式
    invoice_type = Invoice.objects.filter(contract_id=sale_contract_id, is_deleted=0).values('invoice_type')[0]['invoice_type']
    invoice_type = eval(invoice_type)
    # 发票类型
    invoice_category = Invoice.objects.filter(contract_id=sale_contract_id, is_deleted=0).values('invoice_category')[0]['invoice_category']
    invoice_category = eval(invoice_category)

    '''
    下面根据B公司支持的任务类型，查询开票内容（暂时仅查临时个体的任务类型）
    '''
    # 查询销售合同对应的临时个体产品id
    sale_lg_product_data_id = \
        ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1,
                                    tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']
    # 查询临时个体任务支持的任务类型
    sale_lg_task_type = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_task_type')[0][
        'sale_task_type']
    # 任务类型字段存的格式为'1，4，7'，转成tuple随机取其中一个
    sale_lg_task_type = random.choice(eval(sale_lg_task_type))
    # 查询销售合同中的V的id，在查询任务类型和开票内容的关联关系中用到
    v_corpid = Contract.objects.filter(id=sale_contract_id).values('party_b_corp_id')[0]['party_b_corp_id']
    # 根据v_corpid、sale_lg_task_type查询task_type_invoice_content表中的invoice_content_id（开票内容id）,暂时将查询结果根据id倒序，且取第一个
    invoice_content_id = \
    TaskTypeInvoiceContent.objects.filter(task_type_id=sale_lg_task_type, create_corp_id=v_corpid,
                                            is_deleted=0).order_by('-id')[:1].values('invoice_content_id')[0][
        'invoice_content_id']
    # 在根据开票内容id去invoice_content获取开票内容
    invoice_content = InvoiceContent.objects.filter(id=invoice_content_id).values('invoice_content')[0]['invoice_content']
    params = {}
    params['invoice_type'] = invoice_type
    params['invoice_category'] = invoice_category
    params['invoice_content'] = invoice_content
    return params