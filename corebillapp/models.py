# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BillingMonth(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    billing_month = models.CharField(max_length=30)
    bill_status = models.SmallIntegerField(blank=True, null=True)
    bill_start_time = models.DateTimeField(blank=True, null=True)
    bill_start_person = models.CharField(max_length=50, blank=True, null=True)
    bill_time = models.DateTimeField(blank=True, null=True)
    bill_person = models.CharField(max_length=50, blank=True, null=True)
    anti_bill_time = models.DateTimeField(blank=True, null=True)
    anti_bill_person = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=100)
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'billing_month'
        app_label = 'corebillapp'


class BillingMonthOperateLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    operate_user_id = models.BigIntegerField()
    operate_username = models.CharField(max_length=100)
    operate_content = models.CharField(max_length=1024)
    create_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'billing_month_operate_log'
        app_label = 'corebillapp'


class ConfirmPaymentLog(models.Model):
    confirm_number = models.CharField(max_length=50)
    confirm_amount = models.DecimalField(max_digits=12, decimal_places=2)
    transfer_number = models.CharField(max_length=50)
    payer_corp_id = models.IntegerField()
    payer_corp_name = models.CharField(max_length=60, blank=True, null=True)
    biz_category = models.CharField(max_length=20)
    biz_name = models.CharField(max_length=20, blank=True, null=True)
    confirm_time = models.DateTimeField()
    confirm_person = models.CharField(max_length=100)
    remark = models.CharField(max_length=255, blank=True, null=True)
    order_number = models.CharField(max_length=60)
    created_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    deleted_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'confirm_payment_log'
        app_label = 'corebillapp'


class ConfirmPaymentSetting(models.Model):
    payee_corp_id = models.BigIntegerField()
    payee_corp_name = models.CharField(max_length=100)
    payment_cycle = models.CharField(max_length=10)
    payment_cycle_type = models.SmallIntegerField()
    biz_category = models.CharField(max_length=20)
    task_type = models.SmallIntegerField()
    revise_range = models.DecimalField(max_digits=4, decimal_places=2)
    allow_revise_range = models.SmallIntegerField()
    allow_auto_confirm = models.SmallIntegerField()
    corp_user_id = models.BigIntegerField(blank=True, null=True)
    corp_user_name = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    deleted_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'confirm_payment_setting'
        unique_together = (('payee_corp_id', 'task_type', 'biz_category'),)
        app_label = 'corebillapp'


class InvoiceData(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_order_detail_number = models.CharField(max_length=100, blank=True, null=True)
    docnr = models.CharField(max_length=255, blank=True, null=True)
    binvdate = models.CharField(max_length=255, blank=True, null=True)
    binvkind = models.CharField(max_length=255, blank=True, null=True)
    binvcode = models.CharField(max_length=255, blank=True, null=True)
    binvnr = models.CharField(max_length=255, blank=True, null=True)
    bmachinenr = models.CharField(max_length=255, blank=True, null=True)
    bcancelled = models.CharField(max_length=255, blank=True, null=True)
    invkind = models.CharField(max_length=255, blank=True, null=True)
    doctype = models.CharField(max_length=255, blank=True, null=True)
    docdate = models.CharField(max_length=255, blank=True, null=True)
    custnr = models.CharField(max_length=255, blank=True, null=True)
    custname = models.CharField(max_length=255, blank=True, null=True)
    custtaxnr = models.CharField(max_length=255, blank=True, null=True)
    custaddrtel = models.CharField(max_length=255, blank=True, null=True)
    custbankacct = models.CharField(max_length=255, blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    memo2 = models.CharField(max_length=255, blank=True, null=True)
    consigner_name = models.CharField(max_length=255, blank=True, null=True)
    consigner_tax_nr = models.CharField(max_length=255, blank=True, null=True)
    shipper_name = models.CharField(max_length=255, blank=True, null=True)
    shipper_tax_nr = models.CharField(max_length=255, blank=True, null=True)
    origin_via_arrival_place = models.CharField(max_length=255, blank=True, null=True)
    vehicle_kind_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_tonnage = models.CharField(max_length=255, blank=True, null=True)
    freight_memo = models.CharField(max_length=255, blank=True, null=True)
    refinvcode = models.CharField(max_length=255, blank=True, null=True)
    refinvnr = models.CharField(max_length=255, blank=True, null=True)
    rednoticenr = models.CharField(max_length=255, blank=True, null=True)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    checker = models.CharField(max_length=255, blank=True, null=True)
    payee = models.CharField(max_length=255, blank=True, null=True)
    sellerbankacct = models.CharField(max_length=255, blank=True, null=True)
    selleraddresstel = models.CharField(max_length=255, blank=True, null=True)
    totalamount = models.CharField(max_length=255, blank=True, null=True)
    totaltax = models.CharField(max_length=255, blank=True, null=True)
    islist = models.CharField(db_column='isList', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tax_deduction = models.CharField(max_length=255, blank=True, null=True)
    print_count = models.CharField(max_length=255, blank=True, null=True)
    inv_stock = models.CharField(max_length=255, blank=True, null=True)
    include_tax = models.CharField(max_length=255, blank=True, null=True)
    uploadstate = models.CharField(max_length=255, blank=True, null=True)
    uploaderrmsg = models.CharField(max_length=255, blank=True, null=True)
    checkcode = models.CharField(max_length=255, blank=True, null=True)
    cipher = models.CharField(max_length=255, blank=True, null=True)
    signed = models.CharField(max_length=255, blank=True, null=True)
    signcode = models.CharField(max_length=255, blank=True, null=True)
    signdate = models.CharField(max_length=255, blank=True, null=True)
    signerrormsg = models.CharField(max_length=255, blank=True, null=True)
    emails = models.CharField(max_length=255, blank=True, null=True)
    sj = models.CharField(max_length=255, blank=True, null=True)
    kpje = models.CharField(max_length=255, blank=True, null=True)
    kpse = models.CharField(max_length=255, blank=True, null=True)
    pdfurl = models.CharField(max_length=255, blank=True, null=True)
    original_doc_nr = models.CharField(max_length=255, blank=True, null=True)
    item_json = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_data'
        app_label = 'corebillapp'


class InvoiceOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_info_id = models.BigIntegerField(blank=True, null=True)
    order_number = models.CharField(max_length=50, blank=True, null=True)
    biz_category = models.CharField(max_length=30, blank=True, null=True)
    payer_corp_name = models.CharField(max_length=50, blank=True, null=True)
    payee_corp_name = models.CharField(max_length=50, blank=True, null=True)
    invoice_order_number = models.CharField(max_length=50, blank=True, null=True)
    invoice_confirm_time = models.DateTimeField(blank=True, null=True)
    invoice_confirm_person = models.CharField(max_length=100, blank=True, null=True)
    invoice_status = models.SmallIntegerField()
    receipt_status = models.SmallIntegerField()
    receipt_confirm_time = models.DateTimeField(blank=True, null=True)
    receipt_confirm_person = models.CharField(max_length=100, blank=True, null=True)
    review_remark = models.CharField(max_length=100, blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)
    update_by = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    source_from = models.SmallIntegerField(blank=True, null=True)
    target_platform = models.SmallIntegerField(blank=True, null=True)
    payer_corp_id = models.BigIntegerField(blank=True, null=True)
    payee_corp_id = models.BigIntegerField(blank=True, null=True)
    prodname = models.CharField(max_length=200, blank=True, null=True)
    taxrate = models.CharField(max_length=30, blank=True, null=True)
    goodstaxno = models.CharField(max_length=100, blank=True, null=True)
    request_msg = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)
    invoice_type = models.SmallIntegerField(blank=True, null=True)
    invoice_category = models.SmallIntegerField(blank=True, null=True)
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    invoice_content = models.CharField(max_length=100, blank=True, null=True)
    invoice_remark = models.CharField(max_length=200, blank=True, null=True)
    apply_status = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_order'
        unique_together = (('order_info_id', 'is_delete'),)
        app_label = 'corebillapp'


class InvoiceOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_order_id = models.BigIntegerField()
    invoice_order_detail_number = models.CharField(max_length=50)
    machinetaxnr = models.CharField(max_length=255, blank=True, null=True)
    machinenr = models.CharField(max_length=255, blank=True, null=True)
    invkind = models.CharField(max_length=255, blank=True, null=True)
    doctype = models.CharField(max_length=255, blank=True, null=True)
    docnr = models.CharField(max_length=255, blank=True, null=True)
    original_doc_nr = models.CharField(max_length=255, blank=True, null=True)
    docdate = models.CharField(max_length=255, blank=True, null=True)
    custnr = models.CharField(max_length=255, blank=True, null=True)
    custname = models.CharField(max_length=255, blank=True, null=True)
    custtaxnr = models.CharField(max_length=255, blank=True, null=True)
    custaddrtel = models.CharField(max_length=255, blank=True, null=True)
    custbankacct = models.CharField(max_length=255, blank=True, null=True)
    memo = models.CharField(max_length=255, blank=True, null=True)
    memo2 = models.CharField(max_length=255, blank=True, null=True)
    refinvcode = models.CharField(max_length=255, blank=True, null=True)
    refinvnr = models.CharField(max_length=255, blank=True, null=True)
    rednoticenr = models.CharField(max_length=255, blank=True, null=True)
    issuer = models.CharField(max_length=255, blank=True, null=True)
    checker = models.CharField(max_length=255, blank=True, null=True)
    payee = models.CharField(max_length=255, blank=True, null=True)
    sellerbankacct = models.CharField(max_length=255, blank=True, null=True)
    selleraddresstel = models.CharField(max_length=255, blank=True, null=True)
    consigner_name = models.CharField(max_length=255, blank=True, null=True)
    consigner_tax_nr = models.CharField(max_length=255, blank=True, null=True)
    shipper_name = models.CharField(max_length=255, blank=True, null=True)
    shipper_tax_nr = models.CharField(max_length=255, blank=True, null=True)
    origin_via_arrival_place = models.CharField(max_length=255, blank=True, null=True)
    vehicle_kind_no = models.CharField(max_length=255, blank=True, null=True)
    vehicle_tonnage = models.CharField(max_length=255, blank=True, null=True)
    freight_memo = models.CharField(max_length=255, blank=True, null=True)
    tax_deduction = models.CharField(max_length=255, blank=True, null=True)
    list_name = models.CharField(max_length=255, blank=True, null=True)
    emails = models.CharField(max_length=255, blank=True, null=True)
    sj = models.CharField(max_length=255, blank=True, null=True)
    item_json = models.TextField(blank=True, null=True)
    print_status = models.SmallIntegerField()
    invoice_status = models.SmallIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    amount = models.CharField(max_length=50, blank=True, null=True)
    request_msg = models.CharField(max_length=255, blank=True, null=True)
    invoice_time = models.DateTimeField(blank=True, null=True)
    print_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_order_detail'
        app_label = 'corebillapp'


class InvoiceOrderLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_order_id = models.BigIntegerField()
    before_status = models.SmallIntegerField(blank=True, null=True)
    after_status = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_order_log'
        app_label = 'corebillapp'


class InvoicePrintLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_order_id = models.BigIntegerField()
    req_parm = models.TextField(blank=True, null=True)
    rsp_data = models.TextField(blank=True, null=True)
    is_rpc = models.SmallIntegerField(blank=True, null=True)
    req_name = models.CharField(max_length=500, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_print_log'
        app_label = 'corebillapp'


class OrderBatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_batch_number = models.CharField(unique=True, max_length=60)
    task_type = models.SmallIntegerField(blank=True, null=True)
    work_type = models.BigIntegerField(blank=True, null=True)
    work_type_name = models.CharField(max_length=50, blank=True, null=True)
    biz_category = models.CharField(max_length=20, blank=True, null=True)
    apply_task_name = models.TextField(blank=True, null=True)
    apply_work_count = models.IntegerField(blank=True, null=True)
    apply_work_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    apply_corp_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    customer_type = models.SmallIntegerField(blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=128, blank=True, null=True)
    corp_id = models.BigIntegerField(blank=True, null=True)
    corp_name = models.CharField(max_length=128, blank=True, null=True)
    work_key = models.CharField(max_length=255, blank=True, null=True)
    voucher_key = models.CharField(max_length=255, blank=True, null=True)
    service_time = models.CharField(max_length=32, blank=True, null=True)
    notice_time = models.DateTimeField(blank=True, null=True)
    notice_data = models.CharField(max_length=1024, blank=True, null=True)
    notice_status = models.SmallIntegerField(blank=True, null=True)
    notice_success_time = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    is_deleted = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_batch'
        app_label = 'corebillapp'


class OrderBatchAuthLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_batch_number = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    log_remark = models.TextField()
    created_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.SmallIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_batch_auth_log'
        app_label = 'corebillapp'


class OrderInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_batch_number = models.CharField(max_length=50)
    order_number = models.CharField(unique=True, max_length=50)
    biz_type = models.CharField(max_length=20)
    contract_id = models.BigIntegerField(blank=True, null=True)
    product_data_id = models.BigIntegerField(blank=True, null=True)
    contract_type = models.CharField(max_length=20)
    extend_contract_type = models.CharField(max_length=20, blank=True, null=True)
    corp_name = models.CharField(max_length=100, blank=True, null=True)
    payer_corp_id = models.BigIntegerField()
    payer_corp_name = models.CharField(max_length=100)
    payer_bank_name = models.CharField(max_length=100, blank=True, null=True)
    payer_bank_number = models.CharField(max_length=100, blank=True, null=True)
    pay_channel = models.CharField(max_length=20, blank=True, null=True)
    inst_out_code = models.CharField(max_length=30, blank=True, null=True)
    agent_bank_code = models.CharField(max_length=30, blank=True, null=True)
    payee_corp_id = models.BigIntegerField()
    payee_corp_name = models.CharField(max_length=100)
    payee_bank_name = models.CharField(max_length=100, blank=True, null=True)
    payee_corp_bank_number = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount_no_increment_vat = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    service_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    before_adjust_service_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    platform_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    platform_fee_no_increment_vat = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    platform_fee_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    increment_fee_rate = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    increment_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    intermediary_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    intermediary_fee_rate = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    intermediary_fee_no_increment_var = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    contract_threshold_rate = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    revise_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    review_time = models.DateTimeField(blank=True, null=True)
    review_user_id = models.BigIntegerField(blank=True, null=True)
    review_username = models.CharField(max_length=60, blank=True, null=True)
    review_status = models.SmallIntegerField(blank=True, null=True)
    review_remark = models.CharField(max_length=255, blank=True, null=True)
    pay_status = models.SmallIntegerField(blank=True, null=True)
    transfer_number = models.CharField(max_length=50, blank=True, null=True)
    confirm_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    invoice_status = models.SmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_by_user_id = models.BigIntegerField(blank=True, null=True)
    apply_remark = models.CharField(max_length=255, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.SmallIntegerField(blank=True, null=True)
    source_from = models.SmallIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    show_time = models.DateTimeField(blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_info'
        app_label = 'corebillapp'

class OrderInvoiceRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_info_id = models.BigIntegerField()
    invoice_order_id = models.BigIntegerField(blank=True, null=True)
    invoice_order_number = models.CharField(max_length=50)
    order_batch_number = models.CharField(max_length=50)
    biz_category = models.CharField(max_length=30)
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'order_invoice_relation'
        app_label = 'corebillapp'

class OfflineInvoiceOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_batch_number = models.CharField(max_length=100, blank=True, null=True)
    import_remark = models.CharField(max_length=200, blank=True, null=True)
    offline_bill_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    apply_invoice_amount = models.DecimalField(max_digits=12, decimal_places=2)
    apply_invoice_status = models.SmallIntegerField()
    invoice_type = models.SmallIntegerField()
    invoice_category = models.SmallIntegerField(blank=True, null=True)
    invoice_content = models.CharField(max_length=100)
    invoice_remark = models.CharField(max_length=200, blank=True, null=True)
    consigner_tax_nr = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_number = models.CharField(max_length=100, blank=True, null=True)
    import_time = models.DateTimeField()
    import_account = models.CharField(max_length=100, blank=True, null=True)
    import_user_id = models.BigIntegerField(blank=True, null=True)
    corp_id = models.BigIntegerField(blank=True, null=True)
    corp_name = models.CharField(max_length=255)
    apply_invoice_time = models.DateTimeField(blank=True, null=True)
    apply_invoice_account = models.CharField(max_length=100, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    is_deleted = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'offline_invoice_order'
        unique_together = (('offline_bill_number', 'is_deleted', 'version'),)
        app_label = 'corebillapp'

class OrderPayLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_batch_number = models.CharField(max_length=50, blank=True, null=True)
    pay_batch_number = models.CharField(max_length=50)
    pay_status = models.SmallIntegerField()
    biz_status = models.SmallIntegerField()
    confirm_time = models.DateTimeField(blank=True, null=True)
    pay_from_corp_id = models.BigIntegerField()
    pay_from_account = models.CharField(max_length=255)
    pay_from_bank_no = models.CharField(max_length=60)
    pay_from_mobile = models.CharField(max_length=20, blank=True, null=True)
    pay_target_corp_id = models.BigIntegerField()
    pay_target_account = models.CharField(max_length=255)
    pay_target_bank_no = models.CharField(max_length=100)
    pay_remark = models.CharField(max_length=255)
    pay_amount = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    transaction_serial_no = models.CharField(max_length=64, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    payment_type = models.CharField(max_length=30)
    pay_time = models.DateTimeField(blank=True, null=True)
    pay_target_account_type = models.SmallIntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'order_pay_log'
        app_label = 'corebillapp'


class OrderPerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    bill_number = models.CharField(max_length=60)
    payer_corp_id = models.BigIntegerField()
    payer_corp_name = models.CharField(max_length=100)
    payee_user_id = models.BigIntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    personal_income_tax = models.DecimalField(max_digits=12, decimal_places=2)
    personal_income_tax_rate = models.DecimalField(max_digits=6, decimal_places=4)
    created_time = models.DateTimeField()
    is_deleted = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.BigIntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'order_person'
        app_label = 'corebillapp'


class OrderRevenue(models.Model):
    id = models.BigAutoField(primary_key=True)
    revenue_number = models.CharField(max_length=100)
    order_batch_number = models.CharField(max_length=100)
    corp_id = models.BigIntegerField()
    corp_type = models.CharField(max_length=20)
    service_time = models.CharField(max_length=30, blank=True, null=True)
    real_pay_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    real_pay_time = models.DateTimeField(blank=True, null=True)
    real_income_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    real_income_time = models.DateTimeField(blank=True, null=True)
    should_pay_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    billing_month = models.CharField(max_length=50, blank=True, null=True)
    pay_status = models.SmallIntegerField(blank=True, null=True)
    billing_month_update_time = models.DateTimeField(blank=True, null=True)
    billing_month_update_by = models.CharField(max_length=30, blank=True, null=True)
    create_by = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    is_valid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'order_revenue'
        app_label = 'corebillapp'


class OutsourceBatchRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_batch_number = models.CharField(max_length=20)
    outsource_import_record_id = models.BigIntegerField()
    order_batch_number = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'outsource_batch_relation'
        unique_together = (('order_batch_number', 'order_number'),)
        app_label = 'corebillapp'


class OutsourceImportBatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_batch_number = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    create_by_user_id = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    customer_corp_id = models.BigIntegerField(blank=True, null=True)
    customer_corp_name = models.CharField(max_length=100)
    owner_corp_id = models.BigIntegerField()
    owner_corp_name = models.CharField(max_length=100)
    vendor_corp_id = models.BigIntegerField(blank=True, null=True)
    vendor_corp_name = models.CharField(max_length=100, blank=True, null=True)
    outsource_corp_id = models.BigIntegerField(blank=True, null=True)
    outsource_corp_name = models.CharField(max_length=100, blank=True, null=True)
    import_remark = models.CharField(max_length=255, blank=True, null=True)
    file_oss_key = models.CharField(max_length=255)
    check_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'outsource_import_batch'
        app_label = 'corebillapp'


class OutsourceImportRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_batch_number = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    create_ty = models.CharField(max_length=50)
    create_by_user_id = models.BigIntegerField()
    create_by_corp_id = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    check_status = models.SmallIntegerField()
    check_result = models.CharField(max_length=255, blank=True, null=True)
    row_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_number = models.CharField(max_length=100, blank=True, null=True)
    service_time = models.CharField(max_length=100, blank=True, null=True)
    work_count = models.CharField(max_length=100, blank=True, null=True)
    work_amount = models.CharField(max_length=10, blank=True, null=True)
    adjustment_work_amount_bv = models.CharField(max_length=10, blank=True, null=True)
    adjustment_work_amount_vv = models.CharField(max_length=10, blank=True, null=True)
    adjustment_work_amount_vo = models.CharField(max_length=10, blank=True, null=True)
    personal_tax_amount = models.CharField(max_length=10, blank=True, null=True)
    personal_tax_amount_bv = models.CharField(max_length=10, blank=True, null=True)
    personal_tax_amount_vv = models.CharField(max_length=10, blank=True, null=True)
    personal_tax_amount_vo = models.CharField(max_length=10, blank=True, null=True)
    personal_social_security_amount = models.CharField(max_length=10, blank=True, null=True)
    corporation_social_security_amount = models.CharField(max_length=10, blank=True, null=True)
    social_security_amount_bv = models.CharField(max_length=10, blank=True, null=True)
    social_security_amount_vv = models.CharField(max_length=10, blank=True, null=True)
    social_security_amount_vo = models.CharField(max_length=10, blank=True, null=True)
    personal_accumulation_fund = models.CharField(max_length=10, blank=True, null=True)
    corporation_accumulation_fund = models.CharField(max_length=10, blank=True, null=True)
    accumulation_fund_bv = models.CharField(max_length=10, blank=True, null=True)
    accumulation_fund_vv = models.CharField(max_length=10, blank=True, null=True)
    accumulation_fund_vo = models.CharField(max_length=10, blank=True, null=True)
    other_fee_bv = models.CharField(max_length=10, blank=True, null=True)
    other_fee_vv = models.CharField(max_length=10, blank=True, null=True)
    other_fee_vo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsource_import_record'
        unique_together = (('import_batch_number', 'row_number'),)
        app_label = 'corebillapp'


class TransactionBankInfo(models.Model):
    corporation_id = models.IntegerField()
    channel = models.CharField(max_length=20)
    account_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_card_number = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    config_data = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    deleted_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_bank_info'
        unique_together = (('bank_card_number', 'corporation_id', 'is_delete'),)
        app_label = 'corebillapp'


class TransactionConfirmInfo(models.Model):
    transfer_number = models.CharField(max_length=50)
    confirm_type = models.SmallIntegerField()
    payer_corp_id = models.IntegerField(blank=True, null=True)
    payer_corp_name = models.CharField(max_length=100, blank=True, null=True)
    payee_corp_id = models.IntegerField()
    confirm_amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2)
    success_time = models.DateTimeField(blank=True, null=True)
    confirm_status = models.SmallIntegerField()
    sensitive_status = models.SmallIntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    transfer_remark = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField()
    deleted_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_confirm_info'
        app_label = 'corebillapp'


class TransactionInfo(models.Model):
    transfer_number = models.CharField(max_length=50, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    transfer_type = models.SmallIntegerField(blank=True, null=True)
    transfer_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency_code = models.CharField(max_length=50, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    success_time = models.DateTimeField(blank=True, null=True)
    owner_account_name = models.CharField(max_length=100, blank=True, null=True)
    owner_bank_name = models.CharField(max_length=100, blank=True, null=True)
    owner_bank_card_number = models.CharField(max_length=50, blank=True, null=True)
    opposite_account_name = models.CharField(max_length=100, blank=True, null=True)
    opposite_bank_name = models.CharField(max_length=100, blank=True, null=True)
    opposite_bank_card_number = models.CharField(max_length=50, blank=True, null=True)
    cashier_number = models.CharField(unique=True, max_length=50, blank=True, null=True)
    transfer_remark = models.CharField(max_length=255, blank=True, null=True)
    transfer_summary = models.CharField(max_length=255, blank=True, null=True)
    transfer_status = models.SmallIntegerField(blank=True, null=True)
    syn_status = models.SmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    deleted_id = models.BigIntegerField(blank=True, null=True)
    source_from = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_info'
        unique_together = (('owner_bank_card_number', 'transfer_number'),)
        app_label = 'corebillapp'


class TransactionQueryFailureLog(models.Model):
    request_json = models.TextField()
    response_json = models.TextField()
    created_time = models.DateTimeField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'transaction_query_failure_log'
        app_label = 'corebillapp'


class TransactionRefundLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    refund_time = models.DateTimeField()
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2)
    transfer_number = models.CharField(max_length=50)
    cashier_number = models.CharField(max_length=50)
    opposite_account_name = models.CharField(max_length=100)
    refund_remark = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    corp_id = models.BigIntegerField()
    is_delete = models.SmallIntegerField()
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    deleted_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_refund_log'
        app_label = 'corebillapp'
