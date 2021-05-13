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

class DbOperate():


    '''
    查询B端所有用户名
    '''
    # def getAllBUserName(self):
    #     allUserName = list(TCorpUser.objects.all().values('username'))
    #     return allUserName


    '''
    根据B端用户名查询大V用户名（主账号）
    '''
    # def getVUserNameByBUserName(self, busrename):
    #     # 查询B登录账号的公司id
    #     b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    #     # 查询该B公司在销售合同中对应的大V公司id
    #     dvCorpId = \
    #         Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
    #                                 status=0).order_by('-id')[:1].values('party_b_corp_id')[0]['party_b_corp_id']
    #     # 根据公司id去t_corp_user查询该公司下的主账号
    #     dvUserName = TCorpUser.objects.filter(corp_id=dvCorpId, level=1, is_delete=0).order_by('-id')[:1].values('username')[0]['username']
    #     params = {}
    #     params['dvUserName'] = dvUserName
    #     return params


    '''
    根据B端用户名查询大V在transaction_bank_info中的信息
    '''
    # def getTransactionBankInfo(self, busrename, dvBankNumber):
    #     # 查询B登录账号的公司id
    #     b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    #     # 查询该B公司在销售合同中对应的大V公司id
    #     dvCorpId = \
    #         Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
    #                                 status=0).order_by('-id')[:1].values('party_b_corp_id')[0]['party_b_corp_id']
    #     # 查询大V在transaction_bank_info中配的手机号，存在config_data字段中
    #     # config_data需根据卡号和corpid共同确定，因为transaction_bank_info中，一个corpid可以配多个卡号，因为可以有多个支付渠道：mybank、merchantsbank
    #     config_data = TransactionBankInfo.objects.filter(corporation_id=dvCorpId, bank_card_number=dvBankNumber, is_delete=0).order_by('-id')[:1].values('config_data')[0]['config_data']
    #     payerMobile = eval(config_data)['mobile']
    #     params = {}
    #     params['payerMobile'] = payerMobile
    #     return params


    '''
    根据busrename获取销售合同产品信息：
    1、产品id  2、任务类型  3、邀请码
    '''
    # def getProductData(self,busrename):
    #     '''
    #     filter表示过滤条件，相当于where条件，可以传多个参数，相当于where后多个条件用and拼接
    #     exclude表示排除条件，即排除符合括号内符合条件的记录，[:1]即切片，表示取第一条
    #     order_by('-id')表示根据id倒序，order_by('id')表示升序
    #     '''
    #
    #     '''
    #     下面查询B销售合同对应的product_id
    #     '''
    #     # 查询B登录账号的公司id
    #     b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    #     # 查询该B公司的销售合同
    #     sale_contract_id = \
    #     Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
    #                             status=0).order_by('-id')[:1].values('id')[0]['id']
    #     # 查询销售合同对应的非全承揽产品id
    #     sale_fc_product_data_id = \
    #     ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1).exclude(
    #         tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']
    #     # 查询销售合同对应的临时个体产品id
    #     sale_lg_product_data_id = \
    #     ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1,
    #                                tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']
    #
    #     '''
    #     下面查询B公司支持的任务类型
    #     '''
    #     # 查询非全承揽任务支持的任务类型
    #     sale_fc_task_type = ProductData.objects.filter(id=sale_fc_product_data_id).values('sale_task_type')[0][
    #         'sale_task_type']
    #     # 任务类型字段存的格式为'1，4，7'，转成tuple返回
    #     sale_fc_task_type = eval(sale_fc_task_type)
    #     # 查询临时个体任务支持的任务类型
    #     sale_lg_task_type = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_task_type')[0][
    #         'sale_task_type']
    #     # 任务类型字段存的格式为'1，4，7'，转成tuple返回
    #     sale_lg_task_type = eval(sale_lg_task_type)
    #
    #     '''
    #     下面查询B公司的邀请码
    #     '''
    #     invitation_code = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_invitation_code')[0][
    #         'sale_invitation_code']
    #
    #     params = {}
    #     params['sale_fc_product_data_id'] = sale_fc_product_data_id
    #     params['sale_lg_product_data_id'] = sale_lg_product_data_id
    #     params['sale_fc_task_type'] = sale_fc_task_type
    #     params['sale_lg_task_type'] = sale_lg_task_type
    #     params['invitation_code'] = invitation_code
    #     return params


    # '''
    # 根据手机号获取user_info信息
    # 身份证、手机号、姓名
    # '''
    # def getUserInfo(self, mobile):
    #     # 查询user_info中的身份证
    #     id_number = UserInfo.objects.filter(username=mobile, user_type='LABOR').values('id_number')[0]['id_number']
    #     # 查询user_info中的姓名
    #     name = UserInfo.objects.filter(username=mobile, user_type='LABOR').values('real_name')[0]['real_name']
    #     params = {}
    #     params['mobile'] = mobile
    #     params['name'] = name
    #     params['id_number'] = id_number
    #     return params


    # '''
    # 根据taskname获取task_order数据
    # '''
    # def getTaskOrder(self,taskname):
    #     # 根据任务名称，获取taskid
    #     taskId = Task.objects.filter(task_name=taskname).order_by('-id')[:1].values('id')[0]['id']
    #     # 根据taskid，获取taskorderid
    #     task_order_id = TaskOrder.objects.filter(task_id=taskId).values('id')[0]['id']
    #     params = {}
    #     params['task_order_id'] = task_order_id
    #     return params


    '''
    根据busrename获取B结算时所需的开票信息
    开票模式、发票类型、开票内容
    '''
    # def getInvoice(self, busrename):
    #     '''
    #     开票信息存在invoice表，因此先获取销售合同id，再根据合同id去invoice表查
    #     注：1、虽然invoice表存了开票模式、发票类型、开票内容，但是只有开票模式、发票类型在invoice表获取，
    #     开票内容的实际逻辑则要通过task_type_invoice_content、task_type_setting、invoice_content三者关联查找
    #     '''
    #
    #     '''
    #     下面根据销售合同id，获取开票模式、发票类型
    #     '''
    #     # 查询B登录账号的公司id
    #     b_corpid = TCorpUser.objects.filter(username=busrename).values('corp_id')[0]['corp_id']
    #     # 查询该B公司的销售合同
    #     sale_contract_id = \
    #         Contract.objects.filter(party_a_corp_id=b_corpid, biz_category='flabor', category='sale', is_delete=0,
    #                                 status=0).order_by('-id')[:1].values('id')[0]['id']
    #     # 查询在销售合同在incoice表中的开票模式、发票类型
    #     # 开票模式
    #     invoice_type = Invoice.objects.filter(contract_id=sale_contract_id, is_deleted=0).values('invoice_type')[0]['invoice_type']
    #     invoice_type = eval(invoice_type)
    #     # 发票类型
    #     invoice_category = Invoice.objects.filter(contract_id=sale_contract_id, is_deleted=0).values('invoice_category')[0]['invoice_category']
    #     invoice_category = eval(invoice_category)
    #
    #     '''
    #     下面根据B公司支持的任务类型，查询开票内容（暂时仅查临时个体的任务类型）
    #     '''
    #     # 查询销售合同对应的临时个体产品id
    #     sale_lg_product_data_id = \
    #         ProductData.objects.filter(contract_id=sale_contract_id, biz_category='flabor', is_delete=0, status=1,
    #                                    tax_rate_calculation_method=1).order_by('-id')[:1].values('id')[0]['id']
    #     # 查询临时个体任务支持的任务类型
    #     sale_lg_task_type = ProductData.objects.filter(id=sale_lg_product_data_id).values('sale_task_type')[0][
    #         'sale_task_type']
    #     # 任务类型字段存的格式为'1，4，7'，转成tuple随机取其中一个
    #     sale_lg_task_type = random.choice(eval(sale_lg_task_type))
    #     # 查询销售合同中的V的id，在查询任务类型和开票内容的关联关系中用到
    #     v_corpid = Contract.objects.filter(id=sale_contract_id).values('party_b_corp_id')[0]['party_b_corp_id']
    #     # 根据v_corpid、sale_lg_task_type查询task_type_invoice_content表中的invoice_content_id（开票内容id）,暂时将查询结果根据id倒序，且取第一个
    #     invoice_content_id = \
    #     TaskTypeInvoiceContent.objects.filter(task_type_id=sale_lg_task_type, create_corp_id=v_corpid,
    #                                           is_deleted=0).order_by('-id')[:1].values('invoice_content_id')[0][
    #         'invoice_content_id']
    #     # 在根据开票内容id去invoice_content获取开票内容
    #     invoice_content = InvoiceContent.objects.filter(id=invoice_content_id).values('invoice_content')[0]['invoice_content']
    #     params = {}
    #     params['invoice_type'] = invoice_type
    #     params['invoice_category'] = invoice_category
    #     params['invoice_content'] = invoice_content
    #     return params


    # '''
    # 根据taskName获取work表数据
    # '''
    # def getFlaborSettlementWork(self, taskName):
    #     # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    #     taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    #     # 根据taskid查询workid
    #     workId = FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values('work_id')[0]['work_id']
    #     params = {}
    #     params['workId'] = workId
    #     return params


    '''
    查询公司账户余额信息
    '''
    # def getCorpAmount(self,corpUserName):
    #     # 获取企业id
    #     corpId = TCorpUser.objects.filter(username=corpUserName).values('corp_id')[0]['corp_id']
    #     # 获取公司灵工账户余额
    #     flaborBalance = TCorpAccount.objects.filter(corp_id=corpId).values('task_amount')[0]['task_amount']
    #     params = {}
    #     params['flaborBalance'] = flaborBalance
    #     return params


    # '''
    # 根据taskName查询orderinfo信息
    # '''
    # def getOrderInfo(self, taskName):
    #     # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    #     taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    #     # 根据taskid去work表查询订单批次号
    #     batchNumber = FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values('apply_batch_number')[0]['apply_batch_number']
    #     # 根据批次号获取orderinfo中的销售订单总金额
    #     saleTotalAmount = OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values('total_amount')[0]['total_amount']
    #     saleOrderInfoId = \
    #     OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values(
    #         'id')[0]['id']
    #     # 获取采购订单的付款方公司名
    #     buyOrderPayerCorpName = OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values('payer_corp_name')[0]['payer_corp_name']
    #     # 获取采购订单的收款方公司名
    #     buyOrderPayeeCorpName = \
    #     OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
    #         'payee_corp_name')[0]['payee_corp_name']
    #
    #     # 获取采购订单的付款方卡号
    #     buyOrderPayerBankNumber = \
    #     OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
    #         'payer_bank_number')[0]['payer_bank_number']
    #     # 获取采购订单的收款方卡号
    #     buyOrderPayeeBankNumber = \
    #         OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values(
    #             'payee_corp_bank_number')[0]['payee_corp_bank_number']
    #
    #     params = {}
    #     params['saleTotalAmount'] = saleTotalAmount
    #     params['saleOrderInfoId'] = saleOrderInfoId
    #     params['buyOrderPayerCorpName'] = buyOrderPayerCorpName
    #     params['buyOrderPayerBankNumber'] = buyOrderPayerBankNumber
    #     params['buyOrderPayeeCorpName'] = buyOrderPayeeCorpName
    #     params['buyOrderPayeeBankNumber'] = buyOrderPayeeBankNumber
    #     return params


    # '''
    # 根据taskName查询invoice_order信息
    # '''
    # def getInvoiceOrder(self, taskName):
    #     # 根据任务名称获取taskid，可能有任务名相同的情况，根据id降序排，再取最新的一条可解决
    #     taskId = Task.objects.filter(task_name=taskName, is_delete=0).order_by('-id')[:1].values('id')[0]['id']
    #     # 根据taskid去work表查询订单批次号
    #     batchNumber = FlaborSettlementWork.objects.filter(task_id=taskId, is_delete=0).order_by('-id')[:1].values(
    #         'apply_batch_number')[0]['apply_batch_number']
    #     # 根据批次号查询order_info的销售订单id
    #     saleOrderInfoId = OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='sale', is_deleted=0).values('id')[0]['id']
    #     # 根据批次号查询order_info的采购订单id
    #     buyOrderInfoId = \
    #     OrderInfo.objects.filter(order_batch_number=batchNumber, contract_type='buy', is_deleted=0).values('id')[0][
    #         'id']
    #     # 根据order_info_id查询order_invoice_relation表中的关联关系记录，获取invoice_id
    #     saleInvoiceId = OrderInvoiceRelation.objects.filter(order_info_id=saleOrderInfoId, is_deleted=0).values('invoice_order_id')[0]['invoice_order_id']
    #     # 根据order_info_id查询order_invoice_relation表中的关联关系记录，获取invoice_id
    #     buyInvoiceId = \
    #     OrderInvoiceRelation.objects.filter(order_info_id=buyOrderInfoId, is_deleted=0).values('invoice_order_id')[0][
    #         'invoice_order_id']
    #     # 根据invoiceId获取invoice_order的销售订单的order_number
    #     saleOrderNumber = InvoiceOrder.objects.filter(id=saleInvoiceId, is_delete=0).values('order_number')[0]['order_number']
    #     # 根据invoiceId获取invoice_order的采购订单的order_number
    #     buyOrderNumber = InvoiceOrder.objects.filter(id=buyInvoiceId, is_delete=0).values('order_number')[0][
    #         'order_number']
    #     params = {}
    #     params['sale_order_number'] = saleOrderNumber
    #     params['buy_order_number'] = buyOrderNumber
    #     return params