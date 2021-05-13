# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CityAliHumanrun(models.Model):
    id = models.BigAutoField(primary_key=True)
    ali_code = models.IntegerField(blank=True, null=True)
    humanrun_code = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=32, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city_ali_humanrun'
        app_label = 'flaborapp'


class CorpTaskType(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField(blank=True, null=True)
    task_types = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_task_type'
        app_label = 'flaborapp'


class CtUserRegister(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_user_identification = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=100)
    company_code = models.CharField(max_length=30)
    ext_json = models.CharField(max_length=1024, blank=True, null=True)
    contract_url = models.CharField(max_length=4096)
    identity_front_pic_url = models.CharField(max_length=4096, blank=True, null=True)
    identity_back_pic_url = models.CharField(max_length=4096, blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=30, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=30, blank=True, null=True)
    deleted_id = models.BigIntegerField(blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ct_user_register'
        unique_together = (('company_user_identification', 'company_code', 'is_deleted'),)
        app_label = 'flaborapp'


class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback_content = models.CharField(max_length=300, blank=True, null=True)
    feedback_date = models.DateTimeField(blank=True, null=True)
    phone_type = models.CharField(max_length=50, blank=True, null=True)
    browser_type = models.CharField(max_length=50, blank=True, null=True)
    network_type = models.CharField(max_length=50, blank=True, null=True)
    imgs = models.CharField(max_length=2000, blank=True, null=True)
    contract_phone = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_phone = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.CharField(max_length=50, blank=True, null=True)
    page_title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'
        app_label = 'flaborapp'


class FlaborBankInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    account = models.CharField(max_length=255)
    bank_no = models.CharField(max_length=60)
    app_id = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    cert_no = models.CharField(max_length=64, blank=True, null=True)
    partner = models.CharField(max_length=255, blank=True, null=True)
    in_whitelist = models.SmallIntegerField()
    bank_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_bank_info'
        app_label = 'flaborapp'


class FlaborCorpRecharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    corp_name = models.CharField(max_length=200)
    recharge_no = models.CharField(max_length=20)
    recharge_category = models.CharField(max_length=20, blank=True, null=True)
    recharge_channel = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    manage_fee = models.DecimalField(max_digits=10, decimal_places=2)
    states = models.SmallIntegerField()
    voucher_key = models.CharField(max_length=255, blank=True, null=True)
    voucher_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    cashier_no = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    receive_vendor_id = models.BigIntegerField(blank=True, null=True)
    receive_vendor_name = models.CharField(max_length=255, blank=True, null=True)
    receive_vendor_account = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    operation_platform = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_corp_recharge'
        app_label = 'flaborapp'


class FlaborMimeSign(models.Model):
    id = models.BigAutoField(primary_key=True)
    realname = models.CharField(max_length=45)
    mobile = models.CharField(max_length=200)
    idcard = models.CharField(max_length=45)
    contract_type = models.SmallIntegerField()
    corporation_id = models.BigIntegerField(blank=True, null=True)
    vendor_id = models.BigIntegerField()
    bank_card_num = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_area = models.CharField(max_length=50, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    states = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_mime_sign'
        app_label = 'flaborapp'


class FlaborPayBatch(models.Model):
    pay_batch_number = models.CharField(max_length=50)
    pay_status = models.SmallIntegerField()
    biz_status = models.SmallIntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    confirm_time = models.DateTimeField(blank=True, null=True)
    failure_reason = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    pay_from_corp_id = models.IntegerField()
    pay_from_account = models.CharField(max_length=255)
    pay_from_bank_no = models.CharField(max_length=60)
    pay_from_mobile = models.CharField(max_length=20)
    pay_target_corp_id = models.IntegerField()
    pay_target_account = models.CharField(max_length=255)
    pay_target_bank_no = models.CharField(max_length=100)
    pay_remark = models.CharField(max_length=255)
    pay_amount = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    transaction_serial_no = models.CharField(max_length=64, blank=True, null=True)
    payment_type = models.CharField(max_length=30)
    pay_time = models.DateTimeField(blank=True, null=True)
    pay_target_account_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'flabor_pay_batch'
        app_label = 'flaborapp'


class FlaborSettlementExcel(models.Model):
    id = models.BigAutoField(primary_key=True)
    history_id = models.CharField(max_length=64)
    corporation_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    task_name = models.CharField(max_length=200)
    task_source = models.SmallIntegerField()
    realname = models.CharField(max_length=45)
    mobile = models.CharField(max_length=200)
    idcard = models.CharField(max_length=45)
    idcard_type = models.IntegerField()
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    bank_area = models.CharField(max_length=45, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    should_amount = models.DecimalField(max_digits=30, decimal_places=20)
    amount_desc = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    history_type = models.SmallIntegerField()
    states = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    bank_code = models.CharField(max_length=45, blank=True, null=True)
    sms_states = models.SmallIntegerField()
    attr_industry = models.SmallIntegerField(blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    statement_vendor_id = models.BigIntegerField(blank=True, null=True)
    issue_attribute = models.CharField(max_length=4, blank=True, null=True)
    contract_product_id = models.BigIntegerField(blank=True, null=True)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    contract_product_name = models.CharField(max_length=100, blank=True, null=True)
    task_type = models.CharField(max_length=50, blank=True, null=True)
    task_type_id = models.BigIntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_excel'
        app_label = 'flaborapp'


class FlaborSettlementTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    task_type = models.SmallIntegerField()
    task_name = models.CharField(max_length=200)
    corporation_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField()
    issue_attribute = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_task'
        app_label = 'flaborapp'


class FlaborSettlementUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    user_id = models.CharField(max_length=64)
    realname = models.CharField(max_length=45)
    mobile = models.CharField(max_length=200)
    idcard = models.CharField(max_length=45)
    idcard_type = models.IntegerField()
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    bank_code = models.CharField(max_length=45)
    bank_area = models.CharField(max_length=45, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField()
    kh_user_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_user'
        app_label = 'flaborapp'


class FlaborSettlementWork(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    task_name = models.CharField(max_length=200)
    work_id = models.CharField(unique=True, max_length=64)
    corporation_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    user_id = models.CharField(max_length=64)
    realname = models.CharField(max_length=45)
    mobile = models.CharField(max_length=200)
    idcard = models.CharField(max_length=45)
    idcard_type = models.IntegerField()
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    bank_code = models.CharField(max_length=45)
    bank_area = models.CharField(max_length=45, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    should_amount = models.DecimalField(max_digits=30, decimal_places=20)
    amount_desc = models.CharField(max_length=100, blank=True, null=True)
    work_type = models.SmallIntegerField()
    issue_attribute = models.CharField(max_length=4, blank=True, null=True)
    states = models.SmallIntegerField()
    play_no = models.CharField(max_length=45)
    remark = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    apply_success_time = models.DateTimeField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    attr_industry = models.SmallIntegerField(blank=True, null=True)
    kh_user_id = models.CharField(max_length=64, blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    statement_vendor_id = models.BigIntegerField(blank=True, null=True)
    apply_batch_number = models.CharField(max_length=64, blank=True, null=True)
    contract_product_id = models.BigIntegerField(blank=True, null=True)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    contract_product_name = models.CharField(max_length=100, blank=True, null=True)
    notice_success_time = models.DateTimeField(blank=True, null=True)
    task_type = models.CharField(max_length=50, blank=True, null=True)
    task_type_id = models.BigIntegerField(blank=True, null=True)
    account_bank_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_work'
        app_label = 'flaborapp'


class FlaborSettlementWorkBatch(models.Model):
    apply_batch_number = models.CharField(max_length=50)
    apply_time = models.DateTimeField(blank=True, null=True)
    corporation_id = models.IntegerField()
    corporation_name = models.CharField(max_length=50, blank=True, null=True)
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    task_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    current_account_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    current_reviewing_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    recharge_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    apply_pay_total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    platform_fee = models.DecimalField(max_digits=12, decimal_places=2)
    platform_fee_not_tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pay_service_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    service_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pay_platform_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    review_status = models.SmallIntegerField()
    review_state = models.SmallIntegerField()
    service_charge = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    issue_attribute = models.CharField(max_length=4)
    real_service_charge = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    operation_username = models.CharField(max_length=50, blank=True, null=True)
    review_time = models.DateTimeField(blank=True, null=True)
    vendor_corporation_id = models.IntegerField(blank=True, null=True)
    vendor_rate = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    vendor_id = models.IntegerField()
    appoint_vendor_corp_id = models.IntegerField()
    appoint_vendor_id = models.IntegerField()
    appoint_vendor_name = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    cashier_number = models.CharField(max_length=100, blank=True, null=True)
    failure_reason = models.CharField(max_length=255, blank=True, null=True)
    recharge_number = models.CharField(max_length=30, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    voucher_key = models.CharField(max_length=255, blank=True, null=True)
    voucher_url = models.CharField(max_length=255, blank=True, null=True)
    pay_batch_number = models.CharField(max_length=50, blank=True, null=True)
    pay_status = models.SmallIntegerField(blank=True, null=True)
    biz_pay_status = models.SmallIntegerField(blank=True, null=True)
    out_biz_no = models.CharField(max_length=100, blank=True, null=True)
    type = models.SmallIntegerField()
    biz_review_status = models.SmallIntegerField()
    biz_review_time = models.DateTimeField(blank=True, null=True)
    is_rollback = models.SmallIntegerField()
    re_pay_status = models.SmallIntegerField()
    notice_status = models.SmallIntegerField(blank=True, null=True)
    notice_total_count = models.IntegerField(blank=True, null=True)
    notice_time = models.DateTimeField(blank=True, null=True)
    notice_data = models.CharField(max_length=1024, blank=True, null=True)
    apply_username = models.CharField(max_length=50, blank=True, null=True)
    apply_user_id = models.BigIntegerField(blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)
    product_data_id = models.BigIntegerField(blank=True, null=True)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    contract_product_name = models.CharField(max_length=100, blank=True, null=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    channel_name = models.CharField(max_length=100, blank=True, null=True)
    contract_service_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_work_batch'
        app_label = 'flaborapp'


class FlaborSettlementWorkHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    apply_batch_number = models.CharField(max_length=50)
    task_id = models.BigIntegerField()
    task_name = models.CharField(max_length=200)
    work_id = models.CharField(max_length=64)
    corporation_id = models.BigIntegerField()
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    corp_user_id = models.BigIntegerField()
    user_id = models.CharField(max_length=64)
    realname = models.CharField(max_length=45)
    mobile = models.CharField(max_length=200)
    idcard = models.CharField(max_length=45)
    idcard_type = models.IntegerField()
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    bank_code = models.CharField(max_length=45)
    bank_area = models.CharField(max_length=45, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_desc = models.CharField(max_length=100, blank=True, null=True)
    work_type = models.SmallIntegerField()
    issue_attribute = models.CharField(max_length=4, blank=True, null=True)
    states = models.SmallIntegerField()
    play_no = models.CharField(max_length=45)
    remark = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    attr_industry = models.SmallIntegerField(blank=True, null=True)
    kh_user_id = models.CharField(max_length=64, blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    statement_vendor_id = models.BigIntegerField(blank=True, null=True)
    task_type = models.CharField(max_length=50, blank=True, null=True)
    task_type_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_settlement_work_history'
        app_label = 'flaborapp'


class FlaborTaskForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    form_key = models.CharField(max_length=255, blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    parent_sort = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_task_form'
        app_label = 'flaborapp'


class FlaborTaskType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_task_type'
        app_label = 'flaborapp'


class FlaborTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descripe = models.CharField(max_length=500, blank=True, null=True)
    type = models.SmallIntegerField()
    tem_excel = models.CharField(max_length=100)
    header_data = models.CharField(max_length=500)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flabor_template'
        app_label = 'flaborapp'


class LaborFaceCheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    vendor_id = models.BigIntegerField()
    order_no = models.CharField(max_length=64)
    name = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_face_check'
        app_label = 'flaborapp'


class LaborUserBank(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    mobile = models.CharField(max_length=45)
    real_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=45)
    account_type = models.CharField(max_length=10)
    bank_card_num = models.CharField(max_length=100)
    bank = models.CharField(max_length=100, blank=True, null=True)
    subbranch = models.CharField(max_length=100, blank=True, null=True)
    subbranch_city = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labor_user_bank'
        app_label = 'flaborapp'


class NewLabor(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    corp_id = models.BigIntegerField()
    city_name = models.CharField(max_length=1024, blank=True, null=True)
    task_content = models.CharField(max_length=2000, blank=True, null=True)
    task_address = models.CharField(max_length=50, blank=True, null=True)
    task_tags = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)
    city_code = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    task_form = models.CharField(max_length=255)
    task_sort = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_labor'
        app_label = 'flaborapp'


class NewLaborCorp(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    corp_des = models.CharField(max_length=100, blank=True, null=True)
    corp_detail = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_labor_corp'
        app_label = 'flaborapp'


class NewLaborOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_labor_order'
        app_label = 'flaborapp'


class NewLaborTaskType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_delete = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'new_labor_task_type'
        app_label = 'flaborapp'


class NoticeManager(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    batch_no = models.CharField(max_length=64)
    import_time = models.DateTimeField()
    template_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    concat_mode = models.CharField(max_length=50)
    notice_content = models.CharField(max_length=500, blank=True, null=True)
    notice_status = models.SmallIntegerField()
    notice_nums = models.IntegerField()
    notice_channel_flag = models.SmallIntegerField()
    notice_channel = models.CharField(max_length=20, blank=True, null=True)
    notice_time = models.DateTimeField(blank=True, null=True)
    task_name = models.CharField(max_length=100)
    real_issue_money = models.DecimalField(max_digits=16, decimal_places=2)
    task_money = models.DecimalField(max_digits=16, decimal_places=2)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    num = models.DecimalField(max_digits=16, decimal_places=2)
    finish_reward = models.DecimalField(max_digits=16, decimal_places=2)
    first_month_finish_reward = models.DecimalField(max_digits=16, decimal_places=2)
    float_reward = models.DecimalField(max_digits=16, decimal_places=2)
    adjustment = models.DecimalField(max_digits=16, decimal_places=2)
    traffic_subsidy = models.DecimalField(max_digits=16, decimal_places=2)
    should_issue_reward = models.DecimalField(max_digits=16, decimal_places=2)
    personal_tax = models.DecimalField(max_digits=16, decimal_places=2)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice_manager'
        app_label = 'flaborapp'


class NoticeTransfer(models.Model):
    id = models.BigAutoField(primary_key=True)
    notice_id = models.BigIntegerField()
    transfer_id = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice_transfer'
        app_label = 'flaborapp'


class ProductCorpIdTmp(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    corp_id = models.IntegerField(blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    contract_name = models.CharField(max_length=255, blank=True, null=True)
    contract_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_corp_id_tmp'
        app_label = 'flaborapp'


class QuestionnaireLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire_log'
        app_label = 'flaborapp'


class SettlementWhiteList(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField()
    business_module = models.SmallIntegerField()
    task_type = models.SmallIntegerField(blank=True, null=True)
    settlement_need_transfer = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_white_list'
        app_label = 'flaborapp'


class StatementPushNotice(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.CharField(max_length=64)
    out_biz_no = models.CharField(max_length=64)
    out_biz_type = models.CharField(max_length=6)
    old_out_biz_no = models.CharField(max_length=64, blank=True, null=True)
    merchant_id = models.CharField(max_length=100)
    merchant_name = models.CharField(max_length=100)
    payee_account = models.CharField(max_length=100)
    total_count = models.CharField(max_length=10)
    total_amount = models.CharField(max_length=16)
    service_charge = models.CharField(max_length=32)
    compute_service_charge = models.CharField(max_length=32, blank=True, null=True)
    service_rate = models.CharField(max_length=16)
    platform_fee = models.CharField(max_length=16)
    insurance = models.CharField(max_length=16)
    insurance_rate = models.CharField(max_length=16)
    tax = models.CharField(max_length=16)
    tax_rate = models.CharField(max_length=16)
    send_date = models.CharField(max_length=19)
    cut_off_time = models.CharField(max_length=19, blank=True, null=True)
    freezing_time = models.CharField(max_length=19)
    push_time = models.DateTimeField(blank=True, null=True)
    push_status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    merchant_industry = models.SmallIntegerField(blank=True, null=True)
    vendor_service_fee_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    vendor_service_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statement_push_notice'
        app_label = 'flaborapp'


class TSmsLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    sms_template = models.CharField(max_length=50)
    reserver_phone = models.CharField(max_length=20, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_sms_log'
        app_label = 'flaborapp'


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    task_type = models.SmallIntegerField()
    invitation_code = models.CharField(max_length=100, blank=True, null=True)
    grab_sheet_audit = models.IntegerField(blank=True, null=True)
    complete_task_check = models.IntegerField(blank=True, null=True)
    exhibition_type = models.SmallIntegerField(blank=True, null=True)
    task_name = models.CharField(max_length=200)
    task_brief = models.CharField(max_length=300, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    work_type = models.SmallIntegerField()
    other_work_type_name = models.CharField(max_length=50, blank=True, null=True)
    require_num = models.IntegerField()
    task_reward = models.DecimalField(max_digits=12, decimal_places=2)
    province_code = models.IntegerField()
    city_code = models.IntegerField()
    area_code = models.IntegerField()
    address = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=2000)
    task_punch_position = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    punch_position_distance = models.IntegerField(blank=True, null=True)
    task_status = models.SmallIntegerField()
    receive_type = models.SmallIntegerField()
    activity_code = models.CharField(max_length=16, blank=True, null=True)
    publish_account = models.CharField(max_length=200, blank=True, null=True)
    audit_account = models.CharField(max_length=200, blank=True, null=True)
    settlement_status = models.SmallIntegerField()
    settlement_time = models.DateTimeField(blank=True, null=True)
    settlement_material = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    created_by_name = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    submit_form = models.CharField(max_length=255, blank=True, null=True)
    settlement_rules = models.CharField(max_length=2000, blank=True, null=True)
    need_material = models.IntegerField(blank=True, null=True)
    need_end_punch = models.IntegerField(blank=True, null=True)
    source_from = models.IntegerField(blank=True, null=True)
    cancel_remark = models.CharField(max_length=255, blank=True, null=True)
    should_or_real = models.SmallIntegerField(blank=True, null=True)
    is_line = models.SmallIntegerField(blank=True, null=True)
    third_no = models.CharField(max_length=255, blank=True, null=True)
    product_data_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'
        app_label = 'flaborapp'


class TaskAcceptance(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_acceptance'
        app_label = 'flaborapp'


class TaskContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_contact'
        app_label = 'flaborapp'


class TaskLaborCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    sex = models.SmallIntegerField()
    degree = models.SmallIntegerField()
    experience = models.SmallIntegerField()
    certificate = models.CharField(max_length=200)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_labor_condition'
        app_label = 'flaborapp'


class TaskLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    task_id = models.BigIntegerField(blank=True, null=True)
    task_order_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    old_status = models.SmallIntegerField(blank=True, null=True)
    new_status = models.SmallIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    des = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_logs'
        app_label = 'flaborapp'


class TaskMaterialType(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    material_name = models.CharField(max_length=50)
    material_attribute = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_material_type'
        app_label = 'flaborapp'


class TaskOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    task_id = models.BigIntegerField()
    exhibition_type = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    getway = models.SmallIntegerField()
    order_time = models.DateTimeField(blank=True, null=True)
    receive_city_code = models.IntegerField(blank=True, null=True)
    receive_province_code = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    order_status = models.SmallIntegerField()
    audit_status = models.SmallIntegerField(blank=True, null=True)
    task_status = models.SmallIntegerField(blank=True, null=True)
    end_status = models.SmallIntegerField(blank=True, null=True)
    acceptance_remark = models.CharField(max_length=200)
    acceptance_name = models.CharField(max_length=255, blank=True, null=True)
    acceptance_time = models.DateTimeField(blank=True, null=True)
    vendor_id = models.BigIntegerField()
    reject_reason = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    alipay_user_id = models.BigIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    new_order_status = models.SmallIntegerField(blank=True, null=True)
    task_reward = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    change_reward = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    source_from = models.SmallIntegerField(blank=True, null=True)
    submit_task_time = models.DateTimeField(blank=True, null=True)
    should_or_real = models.SmallIntegerField(blank=True, null=True)
    acceptance_pdf = models.CharField(max_length=255, blank=True, null=True)
    noti_state = models.SmallIntegerField(blank=True, null=True)
    change_reward_reason = models.CharField(max_length=255, blank=True, null=True)
    order_status_sms_remind = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order'
        app_label = 'flaborapp'


class TaskOrderEvaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_order_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    attitude = models.FloatField(blank=True, null=True)
    skill = models.FloatField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    alipay_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_evaluation'
        app_label = 'flaborapp'


class TaskOrderInsure(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_order_id = models.BigIntegerField()
    status = models.SmallIntegerField()
    insure_time = models.DateTimeField(blank=True, null=True)
    early_warn_time = models.DateTimeField()
    warn_nums = models.IntegerField()
    call_nums = models.IntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_insure'
        app_label = 'flaborapp'


class TaskOrderLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    task_order_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    label_id = models.BigIntegerField()
    label_name = models.CharField(max_length=20)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_label'
        app_label = 'flaborapp'


class TaskOrderMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_order_id = models.BigIntegerField()
    task_material_type_id = models.BigIntegerField()
    material_name = models.CharField(max_length=50)
    material_content = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_order_material'
        app_label = 'flaborapp'


class TaskOrderPunch(models.Model):
    id = models.BigAutoField(primary_key=True)
    punch_type = models.SmallIntegerField()
    task_order_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    punch_position = models.CharField(max_length=200, blank=True, null=True)
    punch_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_punch'
        app_label = 'flaborapp'


class TaskOrderStatement(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_order_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    out_biz_no = models.CharField(max_length=64, blank=True, null=True)
    cut_off_time = models.DateTimeField(blank=True, null=True)
    cut_off_status = models.SmallIntegerField()
    arrive_time = models.DateTimeField(blank=True, null=True)
    vendor_id = models.BigIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_order_statement'
        app_label = 'flaborapp'


class TaskTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.BigIntegerField()
    task_json = models.JSONField()
    condition_json = models.JSONField()
    acceptance_json = models.JSONField()
    task_contact_json = models.JSONField(blank=True, null=True)
    task_order_json = models.JSONField(blank=True, null=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_template'
        app_label = 'flaborapp'


class TechSignInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField()
    customer_type = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    cert_no = models.CharField(max_length=64, blank=True, null=True)
    sign_user_id = models.CharField(max_length=255, blank=True, null=True)
    sign_seal_data = models.TextField(blank=True, null=True)
    third_type = models.SmallIntegerField(blank=True, null=True)
    sign_template_id = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tech_sign_info'
        app_label = 'flaborapp'


class TechTemplateInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_config_id = models.BigIntegerField(unique=True)
    sign_template_id = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tech_template_info'
        app_label = 'flaborapp'


class TempLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    sid = models.BigIntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    bank_code = models.CharField(max_length=255, blank=True, null=True)
    account_bank_code = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_logs'
        app_label = 'flaborapp'


class ThirdUserInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    alipay_uid = models.CharField(max_length=32, blank=True, null=True)
    wechat_uniqueid = models.CharField(max_length=64, blank=True, null=True)
    wechat_openid = models.CharField(max_length=64, blank=True, null=True)
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=500, blank=True, null=True)
    provice = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    user_type_value = models.CharField(max_length=10, blank=True, null=True)
    third_platform_type = models.SmallIntegerField(blank=True, null=True)
    wowoo_uniqueid = models.CharField(max_length=64, blank=True, null=True)
    real_name = models.CharField(max_length=64, blank=True, null=True)
    cert_no = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=16, blank=True, null=True)
    cert_type = models.SmallIntegerField(blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    create_time = models.DateTimeField()
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'third_user_info'
        unique_together = (('alipay_uid', 'third_platform_type', 'version', 'is_delete'),)
        app_label = 'flaborapp'


class TransferOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch_no = models.CharField(max_length=64)
    serial_no = models.CharField(max_length=64)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pay_account_no = models.CharField(max_length=100)
    payer_show_name = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    pay_success_time = models.CharField(max_length=100, blank=True, null=True)
    payee_type = models.SmallIntegerField(blank=True, null=True)
    receive_account_no = models.CharField(max_length=100)
    receive_real_name = models.CharField(max_length=100, blank=True, null=True)
    payment_type = models.CharField(max_length=20, blank=True, null=True)
    transaction_serial_no = models.CharField(max_length=64, blank=True, null=True)
    pay_status = models.SmallIntegerField()
    version = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    created_by = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer_order'
        app_label = 'flaborapp'


class UserBankCheck(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch_number = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    id_card = models.CharField(max_length=50)
    bank_card = models.CharField(max_length=50)
    check_result = models.IntegerField()
    fail_reason = models.CharField(max_length=300, blank=True, null=True)
    import_time = models.DateTimeField(blank=True, null=True)
    corp_id = models.BigIntegerField(blank=True, null=True)
    login_user_id = models.BigIntegerField(blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bank_check'
        app_label = 'flaborapp'


class UserContractSignInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    vendor_corp_id = models.BigIntegerField()
    contract_type = models.SmallIntegerField()
    contract_key = models.CharField(max_length=2000, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    source_from = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_contract_sign_info'
        app_label = 'flaborapp'


class UserContractTmpInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    vendor_corp_id = models.BigIntegerField()
    corp_id = models.BigIntegerField(blank=True, null=True)
    flow_id = models.CharField(max_length=1000, blank=True, null=True)
    invitation_code = models.CharField(max_length=100, blank=True, null=True)
    contract_config_id = models.IntegerField(blank=True, null=True)
    sign_status = models.SmallIntegerField()
    id_number = models.CharField(max_length=50, blank=True, null=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    task_type = models.SmallIntegerField(blank=True, null=True)
    silent_sign = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'user_contract_tmp_info'
        app_label = 'flaborapp'


class UserFaceLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=500)
    status = models.SmallIntegerField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_face_log'
        app_label = 'flaborapp'


class Vendor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=40, blank=True, null=True)
    vendor_full_name = models.CharField(unique=True, max_length=255)
    vendor_identity = models.CharField(max_length=64, blank=True, null=True)
    applicant_name = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    social_credit_code = models.CharField(max_length=64, blank=True, null=True)
    organization_code = models.CharField(max_length=64, blank=True, null=True)
    regcode = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=100, blank=True, null=True)
    support_apply_mode = models.CharField(max_length=200, blank=True, null=True)
    increase_tax_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estimate_open_tic_num = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    tax_apply_time = models.DateTimeField(blank=True, null=True)
    contract_start_time = models.DateTimeField(blank=True, null=True)
    contract_end_time = models.DateTimeField(blank=True, null=True)
    contract_sign_rlw = models.SmallIntegerField(blank=True, null=True)
    contract_oss_key = models.CharField(max_length=500, blank=True, null=True)
    business_license_oss_key = models.CharField(max_length=500, blank=True, null=True)
    tax_cal_formula_oss_key = models.CharField(max_length=500, blank=True, null=True)
    statement_vendor_id = models.BigIntegerField()
    corp_id = models.BigIntegerField()
    sign_short_chain = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor'
        app_label = 'flaborapp'


class VendorContractConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.BigIntegerField()
    contract_content_html = models.TextField()
    contract_oss_url = models.CharField(max_length=3000)
    type = models.SmallIntegerField(blank=True, null=True)
    delete_id = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    version = models.CharField(max_length=10)
    created_by = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_contract_config'
        app_label = 'flaborapp'


class WorkBatchRelation(models.Model):
    apply_batch_number = models.CharField(max_length=64)
    sh_apply_batch_number = models.CharField(max_length=64)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'work_batch_relation'
        app_label = 'flaborapp'
