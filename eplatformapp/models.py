# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContractSignConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_name = models.CharField(max_length=100, blank=True, null=True)
    contract_oss_url = models.CharField(max_length=3000)
    sign_template_id = models.CharField(max_length=255, blank=True, null=True)
    delete_id = models.BigIntegerField()
    is_deleted = models.SmallIntegerField()
    version = models.CharField(max_length=10)
    created_by = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_sign_config'
        app_label = 'eplatformapp'


class GatewayApiDefine(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    path = models.CharField(max_length=255)
    service_id = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    retryable = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField()
    strip_prefix = models.IntegerField(blank=True, null=True)
    api_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateway_api_define'
        app_label = 'eplatformapp'


class TBillDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField(db_column='corporation_Id')  # Field name made lowercase.
    bill_serial_number = models.CharField(max_length=18)
    bill_date = models.CharField(max_length=8)
    bill_name = models.CharField(max_length=128, blank=True, null=True)
    customer_name = models.CharField(max_length=128, blank=True, null=True)
    reference_total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    value_added_tax_fee_total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    additional_tax_fee_total = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    download_key = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bill_detail'
        app_label = 'eplatformapp'


class TCorpAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    account_no = models.CharField(unique=True, max_length=200)
    pay_password = models.CharField(max_length=64, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=14, decimal_places=2)
    reference_amount = models.DecimalField(max_digits=14, decimal_places=2)
    sms_amount = models.DecimalField(max_digits=14, decimal_places=2)
    task_amount = models.DecimalField(max_digits=14, decimal_places=2)
    outsource_amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    corp_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_account'
        app_label = 'eplatformapp'


class TCorpAccountOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_no = models.CharField(max_length=200)
    type = models.SmallIntegerField()
    product_desc = models.CharField(max_length=512, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_delete = models.SmallIntegerField()
    oss_key = models.CharField(max_length=700, blank=True, null=True)
    file_type = models.SmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    category = models.SmallIntegerField(blank=True, null=True)
    corp_user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_account_order'
        app_label = 'eplatformapp'


class TCorpAuthorizationConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_corp_authorization_config'
        app_label = 'eplatformapp'


class TCorpAuthorizationRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    corp_user_id = models.BigIntegerField()
    authorization_name = models.CharField(max_length=50, blank=True, null=True)
    used_status = models.SmallIntegerField()
    oss_key = models.CharField(max_length=600, blank=True, null=True)
    information_name = models.CharField(max_length=100, blank=True, null=True)
    information_key = models.CharField(max_length=600, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    auth_id = models.BigIntegerField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_authorization_records'
        app_label = 'eplatformapp'


class TCorpUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=200)
    avatar = models.CharField(max_length=2000, blank=True, null=True)
    password = models.CharField(max_length=64)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    level = models.SmallIntegerField()
    parent = models.CharField(max_length=200, blank=True, null=True)
    locked = models.IntegerField()
    name = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    corp_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_user'
        app_label = 'eplatformapp'


class TCorpUserAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    corp_id = models.BigIntegerField()
    account_no = models.CharField(unique=True, max_length=200)
    pay_password = models.CharField(max_length=64, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=14, decimal_places=2)
    reference_amount = models.DecimalField(max_digits=14, decimal_places=2)
    sms_amount = models.DecimalField(max_digits=14, decimal_places=2)
    task_amount = models.DecimalField(max_digits=14, decimal_places=2)
    outsource_amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_user_account'
        app_label = 'eplatformapp'


class TCorpVendorRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    exhibition_type = models.SmallIntegerField(blank=True, null=True)
    task_type = models.SmallIntegerField()
    invitation_code = models.CharField(max_length=100, blank=True, null=True)
    work_type = models.SmallIntegerField(blank=True, null=True)
    contract_start_time = models.DateTimeField(blank=True, null=True)
    contract_end_time = models.DateTimeField(blank=True, null=True)
    contract_oss_key = models.CharField(max_length=500, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    vendor_service_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_vendor_relation'
        app_label = 'eplatformapp'


class TCorpVendorRelationTmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    exhibition_type = models.SmallIntegerField(blank=True, null=True)
    task_type = models.SmallIntegerField()
    invitation_code = models.CharField(max_length=100, blank=True, null=True)
    work_type = models.SmallIntegerField(blank=True, null=True)
    contract_start_time = models.DateTimeField(blank=True, null=True)
    contract_end_time = models.DateTimeField(blank=True, null=True)
    contract_oss_key = models.CharField(max_length=500, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corp_vendor_relation_tmp'
        app_label = 'eplatformapp'


class TCorporation(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=2000, blank=True, null=True)
    social_credit_code = models.CharField(max_length=100, blank=True, null=True)
    license_link_key = models.CharField(max_length=2000, blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    tax_number = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=100, blank=True, null=True)
    finance_person = models.CharField(max_length=100, blank=True, null=True)
    finance_contact_info = models.CharField(max_length=100, blank=True, null=True)
    contract_start_time = models.DateTimeField(blank=True, null=True)
    contract_end_time = models.DateTimeField(blank=True, null=True)
    contract_sign_rlw = models.SmallIntegerField(blank=True, null=True)
    contract_oss_key = models.CharField(max_length=500, blank=True, null=True)
    contract_vendor_id = models.BigIntegerField(blank=True, null=True)
    audit_status = models.SmallIntegerField()
    sign_status = models.SmallIntegerField()
    sign_link_key = models.CharField(max_length=700, blank=True, null=True)
    system_logo = models.CharField(max_length=2000, blank=True, null=True)
    copy_right = models.CharField(max_length=200, blank=True, null=True)
    open_diy = models.SmallIntegerField()
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    manager_tax_include = models.SmallIntegerField(blank=True, null=True)
    manager_tax_include_person = models.SmallIntegerField(blank=True, null=True)
    issue_attribute = models.CharField(max_length=8, blank=True, null=True)
    manager_rate = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    increment_tax_rate = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    temp_person_cal_formula = models.SmallIntegerField(blank=True, null=True)
    temp_person_manager_rate = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    temp_person_increment_rate = models.DecimalField(max_digits=16, decimal_places=4, blank=True, null=True)
    industry_label = models.SmallIntegerField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    create_platform = models.CharField(max_length=30, blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)
    payment_attribute = models.CharField(max_length=255, blank=True, null=True)
    corporation_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corporation'
        app_label = 'eplatformapp'


class TCorporationName(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_corporation_name'
        app_label = 'eplatformapp'


class TCreditOpen(models.Model):
    corp_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 't_credit_open'
        app_label = 'eplatformapp'


class TCreditOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    credit_no = models.CharField(max_length=200)
    type = models.SmallIntegerField()
    product_desc = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_credit_order'
        app_label = 'eplatformapp'


class TCreditPay(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    credit_no = models.CharField(unique=True, max_length=200)
    total_limit = models.DecimalField(max_digits=12, decimal_places=2)
    surplus_amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_credit_pay'
        app_label = 'eplatformapp'


class TDistributorCorporation(models.Model):
    distributor = models.OneToOneField(TCorporation, models.DO_NOTHING, primary_key=True)
    corp = models.ForeignKey(TCorporation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_distributor_corporation'
        unique_together = (('distributor', 'corp'),)
        app_label = 'eplatformapp'


class TEntryInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    template_type = models.SmallIntegerField()
    entry_template = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_entry_invitation'
        app_label = 'eplatformapp'


class TEntryMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    invitation_id = models.BigIntegerField()
    material_name = models.CharField(max_length=50)
    material_type = models.SmallIntegerField()
    material_content = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_entry_material'
        app_label = 'eplatformapp'


class TEntrySmsOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    invitation_id = models.BigIntegerField()
    order_no = models.CharField(max_length=50)
    audit_time = models.DateTimeField(blank=True, null=True)
    order_status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_entry_sms_order'
        app_label = 'eplatformapp'


class TEntryTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    template = models.TextField(blank=True, null=True)
    materials = models.JSONField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_entry_template'
        app_label = 'eplatformapp'


class TExtaxPriceWhitelist(models.Model):
    corp_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 't_extax_price_whitelist'
        app_label = 'eplatformapp'


class TFinancialStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=50)
    corp_id = models.BigIntegerField()
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    service_type = models.SmallIntegerField()
    service_description = models.CharField(max_length=128)
    order_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vendor_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    face_recognition_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    order_profit = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    discount_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    actually_pay = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    payment_channel_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    vendor_name = models.CharField(max_length=64, blank=True, null=True)
    pay_serial_number = models.CharField(max_length=32, blank=True, null=True)
    pay_channel = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_financial_statistics'
        app_label = 'eplatformapp'


class TLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    label_name = models.CharField(max_length=50)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_label'
        app_label = 'eplatformapp'


class TLabelAttribute(models.Model):
    id = models.BigAutoField(primary_key=True)
    label_id = models.BigIntegerField(unique=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_label_attribute'
        app_label = 'eplatformapp'


class TLabelWhitelist(models.Model):
    corp_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 't_label_whitelist'
        app_label = 'eplatformapp'


class TMaterialType(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    material_attribute = models.JSONField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_material_type'
        app_label = 'eplatformapp'


class TMenu(models.Model):
    code = models.CharField(unique=True, max_length=5)
    name = models.CharField(max_length=45)
    icon = models.CharField(max_length=50, blank=True, null=True)
    path = models.CharField(max_length=50)
    link = models.SmallIntegerField(blank=True, null=True)
    terminal = models.CharField(max_length=128, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_menu'
        app_label = 'eplatformapp'


class TNoticeRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    corporation_id = models.BigIntegerField(blank=True, null=True)
    corp_user_id = models.BigIntegerField(blank=True, null=True)
    notice_tittle = models.CharField(max_length=128)
    notice_content = models.CharField(max_length=255, blank=True, null=True)
    notice_type = models.IntegerField()
    status = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_notice_record'
        app_label = 'eplatformapp'


class TReferenceAuthorize(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference_no = models.CharField(max_length=50, blank=True, null=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    invitation_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    reference_ids = models.CharField(max_length=100)
    authorize_time = models.DateTimeField(blank=True, null=True)
    label_id = models.BigIntegerField(blank=True, null=True)
    label_name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    value_added_tax = models.DecimalField(max_digits=12, decimal_places=2)
    surcharge = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    authorize_status = models.SmallIntegerField()
    use_status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    reject_reason = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_authorize'
        app_label = 'eplatformapp'


class TReferenceAuthorizeInvitation(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    reference_product_snapshots = models.TextField(blank=True, null=True)
    link_url = models.CharField(max_length=2000)
    type = models.SmallIntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)
    candidate = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_authorize_invitation'
        app_label = 'eplatformapp'


class TReferenceCandidate(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch_no = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_candidate'
        app_label = 'eplatformapp'


class TReferenceLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)
    agency = models.CharField(max_length=20, blank=True, null=True)
    mode = models.CharField(max_length=20, blank=True, null=True)
    invest_result = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_reference_log'
        app_label = 'eplatformapp'


class TReferenceOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    serial_number = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    authorize_id = models.BigIntegerField()
    name = models.CharField(max_length=20)
    id_card = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reference_ids = models.CharField(max_length=100)
    order_status = models.SmallIntegerField()
    pay_status = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    value_added_tax = models.DecimalField(max_digits=12, decimal_places=2)
    surcharge = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    entrust_time = models.DateTimeField(blank=True, null=True)
    complete_time = models.DateTimeField(blank=True, null=True)
    label_id = models.BigIntegerField(blank=True, null=True)
    label_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_order'
        app_label = 'eplatformapp'


class TReferenceProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=500)
    brief = models.CharField(max_length=20, blank=True, null=True)
    shelves = models.SmallIntegerField(blank=True, null=True)
    maintain = models.SmallIntegerField(blank=True, null=True)
    ref_type = models.SmallIntegerField(blank=True, null=True)
    need_material = models.CharField(max_length=20, blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    spec_code = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_product'
        app_label = 'eplatformapp'


class TReferenceProductVendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=50, blank=True, null=True)
    reference_product_id = models.BigIntegerField(blank=True, null=True)
    reference_product_name = models.CharField(max_length=50, blank=True, null=True)
    vendor_service_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_reference_product_vendor'
        app_label = 'eplatformapp'


class TReferenceResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=50)
    reference_product_id = models.BigIntegerField()
    reference_product_name = models.CharField(max_length=50)
    resume_result_collect_id = models.BigIntegerField(blank=True, null=True)
    invest_result = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_result'
        app_label = 'eplatformapp'


class TReferenceTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_user_id = models.BigIntegerField()
    corporation_id = models.BigIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=50)
    reference_ids = models.CharField(max_length=100)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_reference_template'
        app_label = 'eplatformapp'


class TResumeGapCollect(models.Model):
    id = models.BigAutoField(primary_key=True)
    authorize_id = models.BigIntegerField()
    explain_info = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_resume_gap_collect'
        app_label = 'eplatformapp'


class TResumeOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(max_length=50)
    authorize_id = models.BigIntegerField()
    vendor_id = models.BigIntegerField()
    candidate_name = models.CharField(max_length=128)
    gender = models.SmallIntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    certificate_type = models.SmallIntegerField(blank=True, null=True)
    certificate_no = models.CharField(max_length=32, blank=True, null=True)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    complete_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_resume_order'
        app_label = 'eplatformapp'


class TResumeRefCollect(models.Model):
    id = models.BigAutoField(primary_key=True)
    authorize_id = models.BigIntegerField()
    corp_name = models.CharField(max_length=50)
    base_work_info = models.TextField(blank=True, null=True)
    hr_info = models.TextField(blank=True, null=True)
    superior_info = models.TextField(blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_resume_ref_collect'
        app_label = 'eplatformapp'


class TResumeResultCollect(models.Model):
    id = models.BigAutoField(primary_key=True)
    resume_order_id = models.BigIntegerField()
    product_id = models.BigIntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=128, blank=True, null=True)
    product_code = models.CharField(max_length=128, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_package_product = models.SmallIntegerField(blank=True, null=True)
    investigate_result = models.TextField(blank=True, null=True)
    ref_collect_id = models.BigIntegerField(blank=True, null=True)
    corp_name = models.CharField(max_length=128, blank=True, null=True)
    interviewee_info = models.TextField(blank=True, null=True)
    job_identify_info = models.TextField(blank=True, null=True)
    job_performance_info = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_resume_result_collect'
        app_label = 'eplatformapp'


class TRole(models.Model):
    role = models.CharField(max_length=200, blank=True, null=True)
    role_name = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_role'
        app_label = 'eplatformapp'


class TRoleMenu(models.Model):
    role_id = models.IntegerField()
    menu_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 't_role_menu'
        unique_together = (('menu_id', 'role_id'),)
        app_label = 'eplatformapp'


class TServiceAuth(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    service_type = models.CharField(max_length=20)
    service_id = models.BigIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    authed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_service_auth'
        unique_together = (('corp_id', 'service_type', 'service_id'),)
        app_label = 'eplatformapp'


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
        app_label = 'eplatformapp'


class TSmsReferenceRole(models.Model):
    distributor_id = models.BigIntegerField()
    corp_id = models.BigIntegerField()
    contract_corp_id = models.BigIntegerField()
    sms_reference = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 't_sms_reference_role'
        app_label = 'eplatformapp'


class TTransactionFlow(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(unique=True, max_length=50)
    pay_serial_number = models.CharField(max_length=50, blank=True, null=True)
    serial_type = models.SmallIntegerField()
    serial_amount = models.DecimalField(max_digits=12, decimal_places=2)
    serial_status = models.SmallIntegerField()
    serial_descrition = models.CharField(max_length=100, blank=True, null=True)
    channel = models.CharField(max_length=64)
    channel_order_no = models.CharField(max_length=50, blank=True, null=True)
    business_type = models.CharField(max_length=64)
    pay_date = models.DateTimeField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_transaction_flow'
        app_label = 'eplatformapp'


class TUserRole(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    role = models.ForeignKey(TRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_user_role'
        unique_together = (('user_id', 'role'),)
        app_label = 'eplatformapp'


class TUserWhitelist(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_whitelist'
        app_label = 'eplatformapp'


class TVendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_name = models.CharField(max_length=40, blank=True, null=True)
    vendor_full_name = models.CharField(unique=True, max_length=255)
    applicant_name = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vendor'
        app_label = 'eplatformapp'


class TVendorFinancialStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_no = models.CharField(max_length=50, blank=True, null=True)
    service_type = models.SmallIntegerField()
    product_code = models.CharField(max_length=50, blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=50, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_vendor_financial_statistics'
        app_label = 'eplatformapp'


class TVendorUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendor_id = models.BigIntegerField()
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vendor_user'
        app_label = 'eplatformapp'


class TWorkWhitelist(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 't_work_whitelist'
        app_label = 'eplatformapp'


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
        app_label = 'eplatformapp'


class Vendor(models.Model):
    id = models.BigAutoField(primary_key=True)
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
        app_label = 'eplatformapp'
