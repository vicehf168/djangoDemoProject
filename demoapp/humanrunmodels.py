# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AliFinancial(models.Model):
    account_number = models.CharField(primary_key=True, max_length=45)
    yyyymm = models.CharField(max_length=45)
    stime = models.DateTimeField()
    etime = models.DateTimeField()
    type = models.CharField(max_length=45)
    num_in = models.IntegerField()
    amount_in = models.DecimalField(max_digits=10, decimal_places=2)
    num_out = models.IntegerField()
    amount_out = models.DecimalField(max_digits=10, decimal_places=2)
    amount_total = models.DecimalField(max_digits=10, decimal_places=2)
    export_time = models.DateTimeField()
    row_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_financial'
        unique_together = (('account_number', 'yyyymm', 'type'),)
        app_label = 'demoapp'


class AliFinancialItems(models.Model):
    key = models.CharField(primary_key=True, max_length=45)
    zw_no = models.CharField(max_length=45)
    biz_no = models.CharField(max_length=45, blank=True, null=True)
    account_number = models.CharField(max_length=45)
    yyyymm = models.CharField(max_length=45, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)
    transaction_no = models.CharField(max_length=100, blank=True, null=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    action_time = models.DateTimeField(blank=True, null=True)
    target_account = models.CharField(max_length=45, blank=True, null=True)
    amount_in = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_out = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    blance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    channel = models.CharField(max_length=45, blank=True, null=True)
    biz_type = models.CharField(max_length=45, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    row_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_financial_items'
        app_label = 'demoapp'


class AliFinancialItemsDetail(models.Model):
    account = models.CharField(max_length=100)
    stime = models.DateTimeField()
    etime = models.DateTimeField()
    no = models.CharField(max_length=100)
    in_time = models.DateTimeField()
    ali_trade_no = models.CharField(max_length=45, blank=True, null=True)
    ali_serial_no = models.CharField(max_length=45, blank=True, null=True)
    transaction_no = models.CharField(max_length=45, blank=True, null=True)
    bill_type = models.CharField(max_length=45, blank=True, null=True)
    amount_in = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amount_out = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    amount_service = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    channel = models.CharField(max_length=45, blank=True, null=True)
    product = models.CharField(max_length=45, blank=True, null=True)
    target_account = models.CharField(max_length=45, blank=True, null=True)
    target_name = models.CharField(max_length=45, blank=True, null=True)
    bank_trade_no = models.CharField(max_length=45, blank=True, null=True)
    product_name = models.CharField(max_length=45, blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ali_financial_items_detail'
        app_label = 'demoapp'


class AppAd(models.Model):
    position = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    etime = models.DateTimeField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    otherimages = models.TextField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    show_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_ad'
        app_label = 'demoapp'


class AppVersion(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    isdel = models.CharField(max_length=1, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    upgrade_title = models.CharField(max_length=200, blank=True, null=True)
    upgrade_desc = models.TextField(blank=True, null=True)
    upgrade_type = models.CharField(max_length=1)
    is_upgrade = models.CharField(max_length=1)
    app_url = models.CharField(max_length=200, blank=True, null=True)
    app_id = models.CharField(max_length=200)
    online = models.CharField(max_length=1)
    api_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_version'
        app_label = 'demoapp'


class Apppush(models.Model):
    content = models.CharField(max_length=1000, blank=True, null=True)
    app_id = models.CharField(max_length=200, blank=True, null=True)
    client_id = models.CharField(max_length=200, blank=True, null=True)
    alias = models.CharField(max_length=200, blank=True, null=True)
    push_result = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apppush'
        app_label = 'demoapp'


class Area(models.Model):
    area_name = models.CharField(max_length=45, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    name_pinyin = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    citycode = models.CharField(max_length=20, blank=True, null=True)
    adcode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'
        app_label = 'demoapp'


class AuthBankcard(models.Model):
    idcard = models.CharField(primary_key=True, max_length=45)
    realname = models.CharField(max_length=45)
    bankcard = models.CharField(max_length=45)
    cardtype = models.CharField(max_length=45, blank=True, null=True)
    cardlength = models.CharField(max_length=45, blank=True, null=True)
    cardprefixnum = models.CharField(max_length=45, blank=True, null=True)
    cardname = models.CharField(max_length=45, blank=True, null=True)
    bankname = models.CharField(max_length=45, blank=True, null=True)
    banknum = models.CharField(max_length=45, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    logid = models.CharField(max_length=50, blank=True, null=True)
    resp_code = models.CharField(max_length=10, blank=True, null=True)
    auth_code = models.CharField(max_length=10, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_bankcard'
        unique_together = (('idcard', 'realname', 'bankcard'),)
        app_label = 'demoapp'


class AuthIdcard(models.Model):
    idcard = models.CharField(primary_key=True, max_length=45)
    realname = models.CharField(max_length=45)
    channel = models.CharField(max_length=45)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    prefecture = models.CharField(max_length=50, blank=True, null=True)
    addr_code = models.CharField(max_length=10, blank=True, null=True)
    last_code = models.CharField(max_length=10, blank=True, null=True)
    ok = models.IntegerField()
    more_info = models.TextField(blank=True, null=True)
    msg = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_idcard'
        app_label = 'demoapp'


class Bank(models.Model):
    bank_name = models.CharField(max_length=45)
    bank_code = models.CharField(max_length=45)
    bank_img = models.CharField(max_length=2048, blank=True, null=True)
    limitjson = models.TextField(db_column='limitJson', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'bank'
        app_label = 'demoapp'


class BillBank(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_bank'
        app_label = 'demoapp'


class Corp(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)
    intro = models.CharField(max_length=2000, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    income_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payout_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    province = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    credit_assess = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    status = models.CharField(max_length=45)
    group_info_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    isdelete = models.IntegerField()
    contract = models.TextField(blank=True, null=True)
    fadada_customer_id = models.CharField(max_length=200, blank=True, null=True)
    fadada_account = models.CharField(max_length=20, blank=True, null=True)
    allow_fix_money = models.IntegerField(blank=True, null=True)
    flabor_vendor_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp'
        app_label = 'demoapp'


class CorpApplyForTrial(models.Model):
    name = models.CharField(max_length=64)
    phone = models.BigIntegerField(unique=True)
    company = models.CharField(max_length=255)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)
    approved = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_apply_for_trial'
        app_label = 'demoapp'


class CorpCharge(models.Model):
    charge_type = models.IntegerField()
    corp = models.ForeignKey(Corp, models.DO_NOTHING)
    order_id = models.BigIntegerField(blank=True, null=True)
    before_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=2048, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_charge'
        app_label = 'demoapp'


class CorpLogoWall(models.Model):
    corp_id = models.IntegerField()
    seq = models.IntegerField()
    ctime = models.DateTimeField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_logo_wall'
        app_label = 'demoapp'


class CorpRecharge(models.Model):
    corp = models.ForeignKey(Corp, models.DO_NOTHING)
    transaction_no = models.CharField(max_length=32)
    pay_method = models.CharField(max_length=45)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=45)
    remark = models.CharField(max_length=1024, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'corp_recharge'
        app_label = 'demoapp'


class CorpUser(models.Model):
    user_id = models.IntegerField()
    corp_id = models.IntegerField()
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_user'
        app_label = 'demoapp'


class CorpWorkType(models.Model):
    work_type_id = models.IntegerField(blank=True, null=True)
    corp_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_work_type'
        app_label = 'demoapp'


class Demo(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo'
        app_label = 'demoapp'


class Device(models.Model):
    user_id = models.IntegerField()
    devicetoken = models.CharField(max_length=500, blank=True, null=True)
    clientid = models.CharField(max_length=500, blank=True, null=True)
    system = models.CharField(max_length=20, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'device'
        unique_together = (('id', 'user_id'),)
        app_label = 'demoapp'


class EsignContract(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    flow_id = models.CharField(max_length=255)
    status = models.IntegerField(blank=True, null=True)
    sign_url = models.CharField(max_length=255, blank=True, null=True)
    download_url = models.CharField(max_length=255, blank=True, null=True)
    custom_id = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'esign_contract'
        app_label = 'demoapp'


class Exam(models.Model):
    status = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    train_url = models.CharField(max_length=500, blank=True, null=True)
    pass_score = models.IntegerField(blank=True, null=True)
    work_type_category = models.IntegerField(blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam'
        app_label = 'demoapp'


class ExamQuestion(models.Model):
    exam_id = models.IntegerField(blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_question'
        app_label = 'demoapp'


class ExamResult(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    exam_id = models.IntegerField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    right_num = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_result'
        app_label = 'demoapp'


class ExamWorkType(models.Model):
    exam_id = models.IntegerField(blank=True, null=True)
    work_type_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_work_type'
        app_label = 'demoapp'


class ExportWithdraw(models.Model):
    batch_number = models.BigIntegerField(primary_key=True)
    pay_time = models.DateTimeField()
    payer_email = models.CharField(max_length=45)
    payer_name = models.CharField(max_length=45)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    method = models.CharField(max_length=45)
    send = models.IntegerField()
    send_time = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ali_transfer_status = models.CharField(max_length=5, blank=True, null=True)
    success_num = models.IntegerField(blank=True, null=True)
    success_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    back = models.IntegerField()
    redo = models.IntegerField()
    redo_number = models.BigIntegerField(blank=True, null=True)
    redo_by = models.CharField(max_length=45, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'export_withdraw'
        app_label = 'demoapp'


class ExportWithdrawItems(models.Model):
    batch_number = models.ForeignKey(ExportWithdraw, models.DO_NOTHING, db_column='batch_number')
    cash_transaction_no = models.ForeignKey('UserCash', models.DO_NOTHING, db_column='cash_transaction_no')
    payee_account = models.CharField(max_length=45)
    payee_name = models.CharField(max_length=45)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=100)
    ali_transfer_status = models.CharField(max_length=5, blank=True, null=True)
    extend = models.CharField(max_length=45, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_withdraw_items'
        app_label = 'demoapp'


class FadadaAuditCallback(models.Model):
    flag = models.CharField(max_length=10, blank=True, null=True)
    msg = models.CharField(max_length=100, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    no_pass_reason = models.CharField(max_length=100, blank=True, null=True)
    customer_no = models.CharField(max_length=100, blank=True, null=True)
    platform_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fadada_audit_callback'
        app_label = 'demoapp'


class FadadaContractSign(models.Model):
    contract_id = models.CharField(max_length=32)
    transaction_id = models.CharField(max_length=32)
    client_type = models.CharField(max_length=10)
    client_role = models.CharField(max_length=10, blank=True, null=True)
    customer_id = models.CharField(max_length=50)
    doc_title = models.CharField(max_length=100)
    sign_keyword = models.CharField(max_length=50)
    notify_url = models.CharField(max_length=100, blank=True, null=True)
    result = models.CharField(max_length=800, blank=True, null=True)
    ctime = models.DateTimeField()
    sign_type = models.IntegerField(blank=True, null=True)
    return_url = models.CharField(max_length=500, blank=True, null=True)
    callback_param = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fadada_contract_sign'
        app_label = 'demoapp'


class FadadaFaceVerify(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    customer_id = models.CharField(max_length=200, blank=True, null=True)
    transaction_no = models.CharField(max_length=200, blank=True, null=True)
    status = models.PositiveSmallIntegerField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    is_delete = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'fadada_face_verify'
        app_label = 'demoapp'


class FadadaWorkContract(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    contract_id = models.CharField(max_length=32)
    status = models.IntegerField()
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)
    contract_url = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fadada_work_contract'
        unique_together = (('project_id', 'user_id'),)
        app_label = 'demoapp'


class FeedBack(models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    appid = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feed_back'
        app_label = 'demoapp'


class FileRecord(models.Model):
    user_code = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    terminate_date = models.DateField(blank=True, null=True)
    violation_type = models.CharField(max_length=500, blank=True, null=True)
    penalty = models.CharField(max_length=500, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    quit_date = models.DateField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    id_number = models.CharField(max_length=50, blank=True, null=True)
    template_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_record'
        app_label = 'demoapp'


class FileTemplate(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=1024)
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    sign_positon = models.CharField(max_length=50)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_template'
        app_label = 'demoapp'


class GroupInfo(models.Model):
    name = models.CharField(max_length=100)
    ali_partner = models.CharField(max_length=100, blank=True, null=True)
    ali_key = models.CharField(max_length=100, blank=True, null=True)
    ali_payer_email = models.CharField(max_length=100, blank=True, null=True)
    ali_payer_name = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'group_info'
        app_label = 'demoapp'


class HyenaCorpManage(models.Model):
    manager_user_id = models.IntegerField(primary_key=True)
    corp_id = models.IntegerField()
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hyena_corp_manage'
        unique_together = (('manager_user_id', 'corp_id'),)
        app_label = 'demoapp'


class HyenaProArea(models.Model):
    hyena_pro_id = models.IntegerField()
    province_id = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)
    super_user_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hyena_pro_area'
        app_label = 'demoapp'


class HyenaProject(models.Model):
    name = models.CharField(max_length=100)
    corp_id = models.IntegerField()
    number = models.IntegerField()
    left_day = models.IntegerField(blank=True, null=True)
    next_limit = models.CharField(max_length=45, blank=True, null=True)
    right_day = models.IntegerField(blank=True, null=True)
    must_train = models.IntegerField(blank=True, null=True)
    must_agreement = models.IntegerField(blank=True, null=True)
    must_auth = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    manage_user_id = models.IntegerField()
    train_info_url = models.CharField(max_length=1024, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    contract = models.CharField(max_length=400, blank=True, null=True)
    sign_keyword = models.CharField(max_length=100, blank=True, null=True)
    sign_corp_id = models.IntegerField(blank=True, null=True)
    sign_keyword_user = models.CharField(max_length=100, blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    contract_template = models.CharField(max_length=100, blank=True, null=True)
    contract_template_type = models.IntegerField(blank=True, null=True)
    must_idcard = models.IntegerField(blank=True, null=True)
    pro_team_no = models.CharField(max_length=50, blank=True, null=True)
    pro_no = models.CharField(max_length=100, blank=True, null=True)
    sf_network_code = models.CharField(max_length=100, blank=True, null=True)
    sf_supplier_code = models.CharField(max_length=100, blank=True, null=True)
    view_contract = models.IntegerField(blank=True, null=True)
    mast_bankcard = models.IntegerField(blank=True, null=True)
    mast_studentid = models.IntegerField(blank=True, null=True)
    mast_other = models.IntegerField(blank=True, null=True)
    must_faceid = models.IntegerField(blank=True, null=True)
    need_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_project'
        app_label = 'demoapp'


class HyenaRecruit(models.Model):
    hyena_pro_id = models.IntegerField(primary_key=True)
    task_id = models.IntegerField()
    super_user_id = models.IntegerField(blank=True, null=True)
    train_etime = models.DateTimeField(blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_recruit'
        unique_together = (('hyena_pro_id', 'task_id'),)
        app_label = 'demoapp'


class HyenaSalary(models.Model):
    hyena_work_id = models.IntegerField()
    start_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)
    work_time = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    base = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    base_grant = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    traffic = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    temp_low = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subsidy_house = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subsidy_night = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subsidy_other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wages_reissue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subsidy_holiday = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subsidy_holiday_grant = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax_exempt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    work_overtime = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    absence_fined = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    should_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deduct = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deduct_after_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    tax_before = models.DecimalField(max_digits=10, decimal_places=2)
    tax_after = models.DecimalField(max_digits=10, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    modify_salary = models.DecimalField(max_digits=10, decimal_places=2)
    grant_fact = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_is_modify = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    confirm = models.IntegerField(blank=True, null=True)
    fix_time = models.DateField(blank=True, null=True)
    del_field = models.IntegerField(db_column='del', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_salary'
        app_label = 'demoapp'


class HyenaSfnetwork(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    department_code = models.CharField(max_length=100, blank=True, null=True)
    department_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_sfnetwork'
        app_label = 'demoapp'


class HyenaSfnetworkShare(models.Model):
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    work_time = models.CharField(max_length=500, blank=True, null=True)
    work_info = models.CharField(max_length=500, blank=True, null=True)
    work_require = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField()
    uptime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_sfnetwork_share'
        app_label = 'demoapp'


class HyenaSupplier(models.Model):
    supplier_code = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    department_code = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    sf_resource_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_supplier'
        app_label = 'demoapp'


class HyenaSupplierDepartment(models.Model):
    supplier_code = models.CharField(primary_key=True, max_length=20)
    department_code = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'hyena_supplier_department'
        unique_together = (('supplier_code', 'department_code'),)
        app_label = 'demoapp'


class HyenaUserRegion(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_user_region'
        app_label = 'demoapp'


class HyenaWork(models.Model):
    hp_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField()
    user_id = models.IntegerField()
    interview_time = models.DateTimeField(blank=True, null=True)
    interview_addr = models.CharField(max_length=200, blank=True, null=True)
    interview_contacts = models.CharField(max_length=45, blank=True, null=True)
    interview_phone = models.CharField(max_length=45, blank=True, null=True)
    train_etime = models.DateTimeField(blank=True, null=True)
    train_stime = models.DateTimeField(blank=True, null=True)
    train_addr = models.CharField(max_length=200, blank=True, null=True)
    train_contacts = models.CharField(max_length=45, blank=True, null=True)
    train_phone = models.CharField(max_length=45, blank=True, null=True)
    entry_day = models.DateField(blank=True, null=True)
    leave_day = models.DateField(blank=True, null=True)
    work_place = models.CharField(max_length=200, blank=True, null=True)
    work_period = models.CharField(max_length=100, blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    status = models.IntegerField()
    push = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)
    exam_id = models.IntegerField(blank=True, null=True)
    exam_push_time = models.DateTimeField(blank=True, null=True)
    resource_label_two = models.CharField(max_length=100, blank=True, null=True)
    resource_label_three = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    is_all_day = models.IntegerField(blank=True, null=True)
    is_at_school = models.IntegerField(blank=True, null=True)
    probation_stime = models.DateField(blank=True, null=True)
    probation_etime = models.DateField(blank=True, null=True)
    allowance = models.CharField(max_length=50, blank=True, null=True)
    probation_salary = models.CharField(max_length=50, blank=True, null=True)
    total_salary = models.CharField(max_length=50, blank=True, null=True)
    probation_total_salary = models.CharField(max_length=50, blank=True, null=True)
    probation_allowance = models.CharField(max_length=50, blank=True, null=True)
    worktime_system = models.CharField(max_length=200, blank=True, null=True)
    edu_school_name = models.CharField(max_length=100, blank=True, null=True)
    edu_profession = models.CharField(max_length=100, blank=True, null=True)
    sf_sign_contract = models.IntegerField(blank=True, null=True)
    invite_user_id = models.IntegerField(blank=True, null=True)
    push_result_log = models.CharField(max_length=500, blank=True, null=True)
    push_result = models.IntegerField(blank=True, null=True)
    up_supplier_flag = models.IntegerField(blank=True, null=True)
    esign_contract_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_work'
        unique_together = (('task_id', 'user_id'),)
        app_label = 'demoapp'


class HyenaWorkLive(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    hw_id = models.IntegerField()
    day = models.DateField()

    class Meta:
        managed = False
        db_table = 'hyena_work_live'
        unique_together = (('user_id', 'hw_id', 'day'),)
        app_label = 'demoapp'


class HyenaWorkRecord(models.Model):
    hyena_work_id = models.IntegerField()
    start_day = models.DateField(blank=True, null=True)
    end_day = models.DateField(blank=True, null=True)
    work_time = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=45, blank=True, null=True)
    area = models.CharField(max_length=45, blank=True, null=True)
    work_hour = models.IntegerField()
    user_work_hour = models.IntegerField()
    sick = models.IntegerField()
    absence = models.IntegerField()
    abnormal = models.IntegerField()
    modify_work_time = models.IntegerField()
    push = models.IntegerField()
    remark = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_work_record'
        app_label = 'demoapp'


class HyenaWorkTrack(models.Model):
    hw_id = models.PositiveIntegerField()
    status = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hyena_work_track'
        app_label = 'demoapp'


class LaborCompany(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    ctime = models.DateTimeField()
    province_id = models.IntegerField(blank=True, null=True)
    group_info_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_company'
        app_label = 'demoapp'


class LaborCompanyRoleGroup(models.Model):
    labor_company_role_id = models.IntegerField(primary_key=True)
    group_info_id = models.IntegerField()
    labor_company_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'labor_company_role_group'
        unique_together = (('labor_company_role_id', 'group_info_id', 'labor_company_id'),)
        app_label = 'demoapp'


class LaborHealthCertificate(models.Model):
    user_id = models.IntegerField()
    certificate_number = models.CharField(max_length=100, blank=True, null=True)
    photo_front = models.CharField(max_length=200, blank=True, null=True)
    photo_back = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_health_certificate'
        app_label = 'demoapp'


class LaborWorkType(models.Model):
    user_id = models.IntegerField()
    work_type_id = models.IntegerField()
    status = models.CharField(max_length=30, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=400, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    interview_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_work_type'
        app_label = 'demoapp'


class MenuInfo(models.Model):
    menu_type = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    href = models.CharField(max_length=254)
    rule = models.CharField(max_length=254)
    seq = models.IntegerField()
    is_menu = models.IntegerField()
    enabled = models.IntegerField()
    share = models.IntegerField()
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_info'
        app_label = 'demoapp'


class Message(models.Model):
    type = models.CharField(max_length=30, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    message_base_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    client_id = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    message_no = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'
        app_label = 'demoapp'


class MessageBase(models.Model):
    type = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=2048, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_base'
        app_label = 'demoapp'


class MessageContent(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    sms_content = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_content'
        app_label = 'demoapp'


class NotifyAli(models.Model):
    batch_no = models.BigIntegerField(primary_key=True)
    notify_time = models.CharField(max_length=45, blank=True, null=True)
    notify_type = models.CharField(max_length=45, blank=True, null=True)
    notify_id = models.CharField(max_length=45, blank=True, null=True)
    sign_type = models.CharField(max_length=45, blank=True, null=True)
    sign = models.CharField(max_length=45, blank=True, null=True)
    pay_user_id = models.CharField(max_length=45, blank=True, null=True)
    pay_user_name = models.CharField(max_length=45, blank=True, null=True)
    pay_account_no = models.CharField(max_length=45, blank=True, null=True)
    success_details = models.TextField(blank=True, null=True)
    fail_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notify_ali'
        app_label = 'demoapp'


class OrderTrace(models.Model):
    order_id = models.BigIntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    addr = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_trace'
        app_label = 'demoapp'


class Question(models.Model):
    type = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    title_img = models.CharField(max_length=300, blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    answer = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'
        app_label = 'demoapp'


class RandomCode(models.Model):
    code = models.CharField(primary_key=True, max_length=45)
    length = models.IntegerField()
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'random_code'
        app_label = 'demoapp'


class RoleInfo(models.Model):
    role_type = models.CharField(max_length=45)
    name = models.CharField(unique=True, max_length=45)
    remark = models.CharField(max_length=100, blank=True, null=True)
    enabled = models.IntegerField()
    ctime = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_info'
        app_label = 'demoapp'


class RoleMenu(models.Model):
    role = models.ForeignKey(RoleInfo, models.DO_NOTHING)
    menu = models.OneToOneField(MenuInfo, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'role_menu'
        unique_together = (('menu', 'role'),)
        app_label = 'demoapp'


class School(models.Model):
    type = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'school'
        app_label = 'demoapp'


class SeriesDay(models.Model):
    day = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'series_day'
        app_label = 'demoapp'


class Settlement(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    total_money = models.FloatField(blank=True, null=True)
    overtime_hour = models.IntegerField(blank=True, null=True)
    absence_hour = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement'
        app_label = 'demoapp'


class SfImportData(models.Model):
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_import_data'
        app_label = 'demoapp'


class SfImportData201901171448(models.Model):
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=500, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_import_data_201901171448'
        app_label = 'demoapp'


class SfLeaveBatch(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    total_num = models.IntegerField(blank=True, null=True)
    system_code = models.CharField(max_length=45, blank=True, null=True)
    supplier_code = models.CharField(max_length=45, blank=True, null=True)
    list = models.TextField(blank=True, null=True)
    success_num = models.IntegerField(blank=True, null=True)
    ret_msg = models.CharField(max_length=200, blank=True, null=True)
    ret_code = models.CharField(max_length=45, blank=True, null=True)
    fail_data = models.TextField(blank=True, null=True)
    sign = models.CharField(max_length=100, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    dlist = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_leave_batch'
        app_label = 'demoapp'


class SfLeaveDetail(models.Model):
    level_batch = models.ForeignKey(SfLeaveBatch, models.DO_NOTHING)
    epiemp_code = models.CharField(primary_key=True, max_length=45)
    out_date = models.CharField(max_length=45, blank=True, null=True)
    ret_code = models.CharField(max_length=45, blank=True, null=True)
    batch_no = models.CharField(max_length=45, blank=True, null=True)
    error_msg = models.CharField(max_length=200, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=45, blank=True, null=True)
    idcard = models.CharField(max_length=45, blank=True, null=True)
    mobile = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_leave_detail'
        unique_together = (('epiemp_code', 'level_batch'),)
        app_label = 'demoapp'


class SfPushData(models.Model):
    detailid = models.CharField(db_column='detailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    network = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    assigntime = models.CharField(db_column='assignTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resourcetype = models.CharField(db_column='resourceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resourcelabel = models.CharField(db_column='resourceLabel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='idNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(max_length=100, blank=True, null=True)
    businessarea = models.CharField(db_column='businessArea', max_length=100, blank=True, null=True)  # Field name made lowercase.
    businessareaname = models.CharField(db_column='businessAreaName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suppliercode = models.CharField(db_column='supplierCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='projectId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    resource_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_push_data'
        app_label = 'demoapp'


class SfPushData20190120(models.Model):
    detailid = models.CharField(db_column='detailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    network = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    assigntime = models.CharField(db_column='assignTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resourcetype = models.CharField(db_column='resourceType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resourcelabel = models.CharField(db_column='resourceLabel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='idNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(max_length=100, blank=True, null=True)
    businessarea = models.CharField(db_column='businessArea', max_length=100, blank=True, null=True)  # Field name made lowercase.
    businessareaname = models.CharField(db_column='businessAreaName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    suppliercode = models.CharField(db_column='supplierCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    projectid = models.CharField(db_column='projectId', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sf_push_data_20190120'
        app_label = 'demoapp'


class SfPushLog(models.Model):
    wid = models.IntegerField(blank=True, null=True)
    req = models.TextField(blank=True, null=True)
    res = models.TextField(blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sf_push_log'
        app_label = 'demoapp'


class SfSalary(models.Model):
    order_id = models.CharField(max_length=32)
    batch_no = models.CharField(max_length=45, blank=True, null=True)
    salary_no = models.CharField(max_length=45, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    emp_name = models.CharField(max_length=90, blank=True, null=True)
    emp_no = models.CharField(max_length=30, blank=True, null=True)
    lifnr = models.CharField(max_length=30, blank=True, null=True)
    corp_code = models.CharField(max_length=10, blank=True, null=True)
    net_code = models.CharField(max_length=30, blank=True, null=True)
    pro_team_no = models.CharField(max_length=60, blank=True, null=True)
    work_time = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_salary'
        app_label = 'demoapp'


class SfSalaryBatch(models.Model):
    batch_no = models.CharField(primary_key=True, max_length=45)
    batch_date = models.CharField(max_length=8, blank=True, null=True)
    batch_count = models.IntegerField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_month = models.CharField(max_length=30, blank=True, null=True)
    salary_no = models.CharField(max_length=45, blank=True, null=True)
    salary_count = models.IntegerField(blank=True, null=True)
    salary_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_data = models.TextField(blank=True, null=True)
    diff_code = models.CharField(max_length=30, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    ret_code = models.CharField(max_length=10, blank=True, null=True)
    ret_msg = models.CharField(max_length=200, blank=True, null=True)
    fail_order_data = models.TextField(blank=True, null=True)
    notify = models.IntegerField(blank=True, null=True)
    notify_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    notify_reject_reason = models.CharField(max_length=300, blank=True, null=True)
    notify_remark = models.CharField(max_length=1000, blank=True, null=True)
    fix_total = models.IntegerField(blank=True, null=True)
    wt_query_time = models.DateTimeField(blank=True, null=True)
    wt_query_response = models.TextField(blank=True, null=True)
    wt_query_code = models.CharField(max_length=10, blank=True, null=True)
    wt_query_msg = models.CharField(max_length=1024, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_salary_batch'
        app_label = 'demoapp'


class SfSalaryNotify(models.Model):
    salary_no = models.CharField(max_length=45, blank=True, null=True)
    salary_count = models.IntegerField(blank=True, null=True)
    salary_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diff_code = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    pay_date = models.CharField(max_length=10, blank=True, null=True)
    reject_reason = models.CharField(max_length=300, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    clientip = models.CharField(max_length=45, blank=True, null=True)
    sign = models.CharField(max_length=100, blank=True, null=True)
    real = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_salary_notify'
        app_label = 'demoapp'


class SfSalaryResult(models.Model):
    batchno = models.CharField(max_length=60, blank=True, null=True)
    empno = models.CharField(max_length=60, blank=True, null=True)
    empname = models.CharField(max_length=60, blank=True, null=True)
    amount = models.CharField(max_length=60, blank=True, null=True)
    deduct = models.IntegerField(blank=True, null=True)
    deduct_name = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_salary_result'
        app_label = 'demoapp'


class SfStaff(models.Model):
    pro_tem_no = models.CharField(max_length=50, blank=True, null=True)
    import_date = models.CharField(max_length=30, blank=True, null=True)
    epiemp_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    card_type = models.CharField(max_length=2, blank=True, null=True)
    card_no = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    major_code = models.CharField(max_length=30, blank=True, null=True)
    diff_code = models.CharField(max_length=50, blank=True, null=True)
    epiemp_code = models.CharField(max_length=50, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sf_staff'
        app_label = 'demoapp'


class SmsReceive(models.Model):
    sms_type = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    append_id = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    recv_time = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_receive'
        app_label = 'demoapp'


class SmsSender(models.Model):
    phone = models.CharField(max_length=11, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    msgid = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    channel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_sender'
        app_label = 'demoapp'


class StatisContract(models.Model):
    contract_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statis_contract'
        app_label = 'demoapp'


class StatisCorp(models.Model):
    date = models.DateField()
    corp_total_amount = models.IntegerField()
    corp_arrears_amount = models.IntegerField()
    publish_task_amount = models.IntegerField()
    finish_task_amount = models.IntegerField()
    need_labor_amount = models.IntegerField()
    corp_manager_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statis_corp'
        app_label = 'demoapp'


class StatisDaily(models.Model):
    date = models.DateField()
    register_labor = models.IntegerField()
    active_labor = models.IntegerField()
    apply_quatify_labor = models.IntegerField()
    pass_audit_labor = models.IntegerField()
    confirm_settle_amount = models.DecimalField(max_digits=10, decimal_places=2)
    withdraw_amount = models.DecimalField(max_digits=10, decimal_places=2)
    daily_active_orders = models.IntegerField()
    withdraw_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statis_daily'
        app_label = 'demoapp'


class StatisLabor(models.Model):
    date = models.DateField()
    labor_total_amount = models.IntegerField()
    audit_through_amount = models.IntegerField()
    autditing_amount = models.IntegerField()
    pending_audit_amount = models.IntegerField()
    packer_amount = models.IntegerField()
    reception_amount = models.IntegerField()
    sale_promoters_amount = models.IntegerField()
    rxhibition_service_amount = models.IntegerField()
    admin_assistant_amount = models.IntegerField()
    order_accept_labor_amount = models.IntegerField()
    order_finish_labor_amount = models.IntegerField()
    order_amount_per_labor = models.DecimalField(max_digits=10, decimal_places=2)
    not_apply = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statis_labor'
        app_label = 'demoapp'


class StatisMutiple(models.Model):
    date = models.DateField(unique=True, blank=True, null=True)
    day_register_labor = models.IntegerField()
    all_register_labor = models.IntegerField()
    all_auth_labor = models.IntegerField()
    day_active_labor = models.IntegerField()
    day_add_labor = models.IntegerField()
    month_add_labor = models.IntegerField()
    all_add_labor = models.IntegerField()
    day_add_task = models.IntegerField()
    month_add_task = models.IntegerField()
    all_add_task = models.IntegerField()
    month_avg_order = models.IntegerField()
    max_day_order = models.IntegerField()
    day_active_order = models.IntegerField()
    all_finish_order = models.IntegerField()
    day_salary = models.DecimalField(max_digits=10, decimal_places=2)
    month_salary = models.DecimalField(max_digits=10, decimal_places=2)
    all_salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'statis_mutiple'
        app_label = 'demoapp'


class StatisOrder(models.Model):
    date = models.DateField()
    total_amount = models.IntegerField()
    receive_amount = models.IntegerField()
    work_amount = models.IntegerField()
    corp_confirm_amount = models.IntegerField()
    judge_amount = models.IntegerField()
    user_confirm_amount = models.IntegerField()
    finish_amount = models.IntegerField()
    corp_cancel_amount = models.IntegerField()
    user_cancel_amount = models.IntegerField()
    corp_refuse_amount = models.IntegerField()
    finish_order_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statis_order'
        app_label = 'demoapp'


class StatisTask(models.Model):
    date = models.DateField()
    total_amount = models.IntegerField()
    publish_amount = models.IntegerField()
    draft_amount = models.IntegerField()
    close_amount = models.IntegerField()
    start_amount = models.IntegerField()
    end_amount = models.IntegerField()
    accept_rate = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'statis_task'
        app_label = 'demoapp'


class SysDate(models.Model):
    d = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sys_date'
        app_label = 'demoapp'


class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    work_type = models.ForeignKey('WorkType', models.DO_NOTHING, blank=True, null=True)
    corp = models.ForeignKey(Corp, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    work_duration = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=5)
    overtime_wages = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.IntegerField()
    current_number = models.IntegerField()
    province = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    work_place = models.CharField(max_length=400, blank=True, null=True)
    stime = models.DateField(blank=True, null=True)
    etime = models.DateField(blank=True, null=True)
    work_duty = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    english = models.IntegerField(blank=True, null=True)
    rite = models.IntegerField(blank=True, null=True)
    appearance = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=30)
    help_fix = models.IntegerField()
    help = models.IntegerField()
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    work_stime = models.CharField(max_length=45, blank=True, null=True)
    work_etime = models.CharField(max_length=45, blank=True, null=True)
    only_workday = models.IntegerField(blank=True, null=True)
    total_work_days = models.IntegerField(blank=True, null=True)
    work_type_name = models.CharField(max_length=20, blank=True, null=True)
    expected_expenses = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overtime_unit = models.CharField(max_length=5)
    allow_student = models.IntegerField()
    need_work_time = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    work_time_limit = models.IntegerField(blank=True, null=True)
    require_education = models.CharField(max_length=255, blank=True, null=True)
    require_experience = models.CharField(max_length=255, blank=True, null=True)
    salary_range = models.CharField(max_length=255, blank=True, null=True)
    show_salary = models.IntegerField(blank=True, null=True)
    sf_detailid = models.CharField(db_column='sf_detailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sf_resource_type = models.IntegerField(blank=True, null=True)
    sf_projectid = models.CharField(db_column='sf_projectId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    business_area_code = models.CharField(max_length=100, blank=True, null=True)
    sf_network_code = models.CharField(max_length=100, blank=True, null=True)
    sf_supplier_code = models.CharField(max_length=100, blank=True, null=True)
    show_work_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'
        app_label = 'demoapp'


class TaskOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.IntegerField()
    task = models.ForeignKey(Task, models.DO_NOTHING)
    reckon_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_amount_type = models.CharField(max_length=255, blank=True, null=True)
    company_amount = models.DecimalField(max_digits=10, decimal_places=2)
    company_remark = models.TextField(blank=True, null=True)
    company_score = models.CharField(max_length=10, blank=True, null=True)
    company_comment = models.TextField(blank=True, null=True)
    user_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_remark = models.TextField(blank=True, null=True)
    judge_amount = models.DecimalField(max_digits=10, decimal_places=2)
    judge_remark = models.TextField(blank=True, null=True)
    report_time = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=20)
    punctuality = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    assess = models.CharField(max_length=1024, blank=True, null=True)
    work_quality = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    refuse_reason = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order'
        app_label = 'demoapp'


class TaskOrderFreeze(models.Model):
    task_order_id = models.BigIntegerField(primary_key=True)
    freeze_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    freeze = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_freeze'
        app_label = 'demoapp'


class Temp(models.Model):
    d = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temp'
        app_label = 'demoapp'


class Train(models.Model):
    corp_id = models.IntegerField()
    province_id = models.IntegerField()
    city_id = models.IntegerField()
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    survey_explain = models.TextField(blank=True, null=True)
    train_explain = models.TextField(blank=True, null=True)
    exam_explain = models.TextField(blank=True, null=True)
    lectuer = models.CharField(max_length=45, blank=True, null=True)
    organizer = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    train_book_url = models.CharField(max_length=1024, blank=True, null=True)
    exam_id = models.IntegerField(blank=True, null=True)
    exam_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train'
        app_label = 'demoapp'


class TrainDate(models.Model):
    train_id = models.IntegerField()
    class_date = models.DateField()
    class_stime = models.TimeField()
    class_etime = models.TimeField()
    sign_min = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'train_date'
        app_label = 'demoapp'


class TrainDateUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    train_date_id = models.IntegerField()
    sign_time = models.DateTimeField()
    sign_address = models.CharField(max_length=512, blank=True, null=True)
    sgin_longitude = models.CharField(max_length=64, blank=True, null=True)
    sgin_latitude = models.CharField(max_length=64, blank=True, null=True)
    udid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_date_user'
        unique_together = (('user_id', 'train_date_id'),)
        app_label = 'demoapp'


class TrainFeedback(models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    train_id = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)
    train_date_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_feedback'
        app_label = 'demoapp'


class TrainPhoto(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    train_id = models.IntegerField(blank=True, null=True)
    train_date_id = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=512, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    longitude = models.CharField(max_length=64, blank=True, null=True)
    latitude = models.CharField(max_length=64, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)
    udid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_photo'
        app_label = 'demoapp'


class TrainUser(models.Model):
    user_id = models.IntegerField()
    train_id = models.IntegerField(primary_key=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'train_user'
        unique_together = (('train_id', 'user_id'),)
        app_label = 'demoapp'


class UserAli(models.Model):
    user_id = models.IntegerField()
    ali = models.CharField(max_length=100)
    ali_real_name = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_ali'
        app_label = 'demoapp'


class UserBankCard(models.Model):
    user_id = models.IntegerField()
    bank_id = models.IntegerField(blank=True, null=True)
    bank_area = models.CharField(max_length=45, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=50)
    user_real_name = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bank_card'
        app_label = 'demoapp'


class UserCash(models.Model):
    transaction_no = models.CharField(max_length=32)
    user_id = models.IntegerField(blank=True, null=True)
    card_id = models.IntegerField(blank=True, null=True)
    realname = models.CharField(max_length=50, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    account_remark = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=45, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=45)
    remark = models.CharField(max_length=1024, blank=True, null=True)
    extend = models.TextField(blank=True, null=True)
    moreinfo = models.CharField(max_length=1024, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)
    labor_company_id = models.IntegerField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cash'
        app_label = 'demoapp'


class UserCharge(models.Model):
    charge_type = models.IntegerField()
    user_id = models.IntegerField()
    order_id = models.BigIntegerField(blank=True, null=True)
    before_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.CharField(max_length=2048, blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField()
    create_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_charge'
        app_label = 'demoapp'


class UserExtend(models.Model):
    user_id = models.IntegerField(unique=True)
    resume = models.CharField(max_length=1024, blank=True, null=True)
    photo_front = models.CharField(max_length=1024, blank=True, null=True)
    photo_back = models.CharField(max_length=1024, blank=True, null=True)
    photo_education = models.CharField(max_length=1024, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    first = models.IntegerField(blank=True, null=True)
    english = models.IntegerField(blank=True, null=True)
    rite = models.IntegerField(blank=True, null=True)
    appearance = models.IntegerField(blank=True, null=True)
    work_quality = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    ability_level = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    punctuality = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=45, blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    school = models.IntegerField(blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    enroll_date = models.DateField(blank=True, null=True)
    student_card1 = models.CharField(max_length=1024, blank=True, null=True)
    student_card2 = models.CharField(max_length=1024, blank=True, null=True)
    student_auth = models.CharField(max_length=45, blank=True, null=True)
    nation = models.CharField(max_length=50, blank=True, null=True)
    marriage = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    subbranch = models.CharField(max_length=100, blank=True, null=True)
    subbranch_city = models.CharField(max_length=100, blank=True, null=True)
    bank_card_num = models.CharField(max_length=100, blank=True, null=True)
    bank_card_front = models.CharField(max_length=1024, blank=True, null=True)
    birthday = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    native_place_province = models.CharField(max_length=100, blank=True, null=True)
    native_place_city = models.CharField(max_length=100, blank=True, null=True)
    native_addr_province = models.CharField(max_length=200, blank=True, null=True)
    native_addr_city = models.CharField(max_length=200, blank=True, null=True)
    native_type = models.CharField(max_length=50, blank=True, null=True)
    political_status = models.CharField(max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=100, blank=True, null=True)
    firstwork_start_date = models.CharField(max_length=100, blank=True, null=True)
    social_security_place = models.CharField(max_length=200, blank=True, null=True)
    social_security_number = models.CharField(max_length=100, blank=True, null=True)
    fund_number = models.CharField(max_length=100, blank=True, null=True)
    fixed_addr = models.CharField(max_length=200, blank=True, null=True)
    fixed_zipcode = models.CharField(max_length=50, blank=True, null=True)
    home_addr = models.CharField(max_length=200, blank=True, null=True)
    work_start_date = models.CharField(max_length=100, blank=True, null=True)
    work_end_date = models.CharField(max_length=100, blank=True, null=True)
    work_corp_name = models.CharField(max_length=200, blank=True, null=True)
    work_department = models.CharField(max_length=100, blank=True, null=True)
    work_position = models.CharField(max_length=201, blank=True, null=True)
    work_annual_salary = models.CharField(max_length=50, blank=True, null=True)
    work_reterence = models.CharField(max_length=100, blank=True, null=True)
    work_reterence_mobile = models.CharField(max_length=20, blank=True, null=True)
    edu_start_date = models.CharField(max_length=20, blank=True, null=True)
    edu_end_date = models.CharField(max_length=20, blank=True, null=True)
    edu_school_name = models.CharField(max_length=100, blank=True, null=True)
    edu_profession = models.CharField(max_length=50, blank=True, null=True)
    edu_reterence = models.CharField(max_length=50, blank=True, null=True)
    professional_certificate = models.CharField(max_length=1024, blank=True, null=True)
    positional_titles = models.CharField(max_length=100, blank=True, null=True)
    know_language = models.CharField(max_length=50, blank=True, null=True)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)
    computer_level = models.CharField(max_length=50, blank=True, null=True)
    family_member_name = models.CharField(max_length=50, blank=True, null=True)
    family_member_relation = models.CharField(max_length=50, blank=True, null=True)
    family_member_corp = models.CharField(max_length=100, blank=True, null=True)
    family_member_position = models.CharField(max_length=50, blank=True, null=True)
    family_member_mobile = models.CharField(max_length=20, blank=True, null=True)
    other_member_name = models.CharField(max_length=50, blank=True, null=True)
    other_member_relation = models.CharField(max_length=50, blank=True, null=True)
    other_member_mobile = models.CharField(max_length=50, blank=True, null=True)
    family_member_in_baiqian = models.CharField(max_length=10, blank=True, null=True)
    recommend_in_baiqian = models.CharField(max_length=10, blank=True, null=True)
    violator = models.CharField(max_length=10, blank=True, null=True)
    fixed_addr_province = models.IntegerField(blank=True, null=True)
    fixed_addr_city = models.IntegerField(blank=True, null=True)
    home_addr_province = models.IntegerField(blank=True, null=True)
    home_addr_city = models.IntegerField(blank=True, null=True)
    other_certificate = models.CharField(max_length=1024, blank=True, null=True)
    faceid_result = models.IntegerField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    health_certificate = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_extend'
        app_label = 'demoapp'


class UserGroupInfo(models.Model):
    user_id = models.IntegerField(primary_key=True)
    group_info_id = models.IntegerField()
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_group_info'
        unique_together = (('user_id', 'group_info_id'),)
        app_label = 'demoapp'


class UserInfo(models.Model):
    sysname = models.CharField(max_length=45, blank=True, null=True)
    user_type = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    mobile = models.CharField(max_length=45)
    email = models.CharField(max_length=100, blank=True, null=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    id_number = models.CharField(max_length=45, blank=True, null=True)
    authidcard = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=400, blank=True, null=True)
    province = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    addr_extend = models.CharField(max_length=100, blank=True, null=True)
    auth_status = models.CharField(max_length=45)
    account_status = models.CharField(max_length=45)
    remark = models.CharField(max_length=45, blank=True, null=True)
    ctime = models.DateTimeField()
    utime = models.DateTimeField(blank=True, null=True)
    cash_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    income_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payout_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sf_staff_no = models.CharField(max_length=20, blank=True, null=True)
    sf_staff_no_time = models.DateTimeField(blank=True, null=True)
    sf = models.IntegerField(blank=True, null=True)
    sf_pushtime = models.DateTimeField(blank=True, null=True)
    supplier_code = models.CharField(max_length=45, blank=True, null=True)
    from_field = models.CharField(db_column='from', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    update_by = models.CharField(max_length=45, blank=True, null=True)
    app_province_id = models.IntegerField(blank=True, null=True)
    app_city_id = models.IntegerField(blank=True, null=True)
    labor_company_id = models.IntegerField(blank=True, null=True)
    fadada_customer_id = models.CharField(max_length=200, blank=True, null=True)
    invite_code = models.CharField(max_length=10, blank=True, null=True)
    invite_user_id = models.IntegerField(blank=True, null=True)
    auto_accept = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
        app_label = 'demoapp'


class UserLaborCompany(models.Model):
    user_id = models.IntegerField(primary_key=True)
    labor_company_id = models.IntegerField()
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_labor_company'
        unique_together = (('user_id', 'labor_company_id'),)
        app_label = 'demoapp'


class UserLog(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_log'
        app_label = 'demoapp'


class UserRole(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(RoleInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user_id', 'role'),)
        app_label = 'demoapp'


class UserUpdateInfo(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=400, blank=True, null=True)
    id_number = models.CharField(max_length=45, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=45, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    district_id = models.IntegerField(blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    student = models.IntegerField(blank=True, null=True)
    enroll_date = models.DateField(blank=True, null=True)
    student_card1 = models.CharField(max_length=1024, blank=True, null=True)
    student_card2 = models.CharField(max_length=1024, blank=True, null=True)
    school = models.IntegerField(blank=True, null=True)
    photo_education = models.CharField(max_length=1024, blank=True, null=True)
    photo_front = models.CharField(max_length=1024, blank=True, null=True)
    photo_back = models.CharField(max_length=1024, blank=True, null=True)
    addr_extend = models.CharField(max_length=100, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_update_info'
        app_label = 'demoapp'


class UserYm(models.Model):
    user_id = models.IntegerField(primary_key=True)
    ym = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user_ym'
        unique_together = (('user_id', 'ym'),)
        app_label = 'demoapp'


class WihteUser(models.Model):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    realname = models.CharField(max_length=200, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wihte_user'
        app_label = 'demoapp'


class WorkTime(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    task_id = models.IntegerField(blank=True, null=True)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    end_latitude = models.CharField(max_length=50, blank=True, null=True)
    end_longitude = models.CharField(max_length=50, blank=True, null=True)
    end_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_time'
        app_label = 'demoapp'


class WorkType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    need_base_auth = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    utime = models.DateTimeField(blank=True, null=True)
    icon = models.CharField(max_length=500, blank=True, null=True)
    audit_type = models.IntegerField(blank=True, null=True)
    interview = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_type'
        app_label = 'demoapp'
