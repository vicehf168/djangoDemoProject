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
根据taskName查询invoice_order信息
'''
def getInvoiceOrder(taskName):
    # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    # 根据taskid去work表查询订单批次号
    batchNumber = FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values(
        'apply_batch_number')[0]['apply_batch_number']
    # 根据批次号查询order_info的销售订单id
    saleOrderInfoId = \
    OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values('id')[0]['id']
    # 根据批次号查询order_info的采购订单id
    buyOrderInfoId = \
        OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values('id')[0][
            'id']
    # 根据order_info_id查询order_invoice_relation表中的关联关系记录，获取销售invoice_id
    saleInvoiceId = \
    OrderInvoiceRelation.objects.filter(order_info_id=saleOrderInfoId, is_deleted=0).values('invoice_order_id')[0][
        'invoice_order_id']
    # 根据order_info_id查询order_invoice_relation表中的关联关系记录，获取采购invoice_id
    buyInvoiceId = \
        OrderInvoiceRelation.objects.filter(order_info_id=buyOrderInfoId, is_deleted=0).values('invoice_order_id')[0][
            'invoice_order_id']
    # 根据invoiceId获取invoice_order的销售订单的order_number
    saleOrderNumber = InvoiceOrder.objects.filter(id=saleInvoiceId, is_delete=0).values('order_number')[0][
        'order_number']
    # 根据invoiceId获取invoice_order的采购订单的order_number
    buyOrderNumber = InvoiceOrder.objects.filter(id=buyInvoiceId, is_delete=0).values('order_number')[0][
        'order_number']
    params = {}
    params['sale_order_number'] = saleOrderNumber
    params['buy_order_number'] = buyOrderNumber
    return params