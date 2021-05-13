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
根据taskName查询orderinfo信息
'''
def getOrderInfo(taskName):
    # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    # 根据taskid去work表查询订单批次号
    batchNumber = \
    FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values('apply_batch_number')[
        0]['apply_batch_number']
    # 根据批次号获取orderinfo中的销售订单总金额
    saleTotalAmount = \
    OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values('total_amount')[
        0]['total_amount']
    # 根据批次号获取orderinfo中的采购订单总金额
    buyTotalAmount = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
            'total_amount')[
            0]['total_amount']
    # 获取销售订单id
    saleOrderInfoId = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values(
            'id')[0]['id']
    # 获取采购订单id
    buyOrderInfoId = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
            'id')[0]['id']
    # 获取采购订单的付款方公司名
    buyOrderPayerCorpName = \
    OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
        'payer_corp_name')[0]['payer_corp_name']
    # 获取采购订单的收款方公司名
    buyOrderPayeeCorpName = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
            'payee_corp_name')[0]['payee_corp_name']

    # 获取采购订单的付款方卡号
    buyOrderPayerBankNumber = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
            'payer_bank_number')[0]['payer_bank_number']
    # 获取采购订单的收款方卡号
    buyOrderPayeeBankNumber = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
            'payee_corp_bank_number')[0]['payee_corp_bank_number']

    params = {}
    params['saleTotalAmount'] = saleTotalAmount
    params['saleOrderInfoId'] = saleOrderInfoId
    params['buyTotalAmount'] = buyTotalAmount
    params['buyOrderInfoId'] = buyOrderInfoId
    params['buyOrderPayerCorpName'] = buyOrderPayerCorpName
    params['buyOrderPayerBankNumber'] = buyOrderPayerBankNumber
    params['buyOrderPayeeCorpName'] = buyOrderPayeeCorpName
    params['buyOrderPayeeBankNumber'] = buyOrderPayeeBankNumber
    return params