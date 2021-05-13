# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlgorithmSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    algorithm_value = models.SmallIntegerField(unique=True)
    algorithm_label = models.CharField(unique=True, max_length=50)
    algorithm_desc = models.CharField(max_length=1024)
    algorithm_category = models.CharField(max_length=20)
    algorithm_biz_category = models.CharField(max_length=10)
    is_delete = models.SmallIntegerField()
    script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algorithm_setting'
        app_label = 'demoapp'


class Contract(models.Model):
    id = models.BigAutoField(primary_key=True)
    biz_number = models.CharField(max_length=30)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    biz_category = models.CharField(max_length=12)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    party_a_corp_id = models.BigIntegerField()
    party_a_corp_name = models.CharField(max_length=100)
    party_a_contract_person = models.CharField(max_length=50, blank=True, null=True)
    party_a_contract_details = models.CharField(max_length=255, blank=True, null=True)
    party_b_corp_id = models.BigIntegerField()
    party_b_corp_name = models.CharField(max_length=100)
    party_b_contract_person = models.CharField(max_length=50, blank=True, null=True)
    party_b_contract_details = models.CharField(max_length=255, blank=True, null=True)
    party_c_corp_id = models.BigIntegerField(blank=True, null=True)
    party_c_corp_name = models.CharField(max_length=100, blank=True, null=True)
    party_c_contract_person = models.CharField(max_length=50, blank=True, null=True)
    party_c_contract_details = models.CharField(max_length=255, blank=True, null=True)
    pdf_oss_key = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    status = models.SmallIntegerField()
    expires_continue = models.SmallIntegerField(blank=True, null=True)
    continue_begin_time = models.DateTimeField(blank=True, null=True)
    continue_time = models.BigIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    review_status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'contract'
        app_label = 'demoapp'


class ContractBankInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    payer_corp_name = models.CharField(max_length=100, blank=True, null=True)
    payer_corp_id = models.BigIntegerField(blank=True, null=True)
    payer_account_name = models.CharField(max_length=255, blank=True, null=True)
    payer_bank_name = models.CharField(max_length=100, blank=True, null=True)
    payer_bank_number = models.CharField(max_length=100, blank=True, null=True)
    payer_bank_mobile = models.CharField(max_length=100, blank=True, null=True)
    payee_corp_name = models.CharField(max_length=100, blank=True, null=True)
    payee_corp_id = models.BigIntegerField(blank=True, null=True)
    payee_account_name = models.CharField(max_length=255, blank=True, null=True)
    payee_bank_name = models.CharField(max_length=100, blank=True, null=True)
    payee_bank_number = models.CharField(max_length=100, blank=True, null=True)
    payee_bank_mobile = models.CharField(max_length=100, blank=True, null=True)
    payee_inst_out_code = models.CharField(max_length=30, blank=True, null=True)
    contract_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_bank_info'
        app_label = 'demoapp'


class Corporation(models.Model):
    account_id = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    logo = models.CharField(max_length=512, blank=True, null=True)
    license_link_key = models.CharField(max_length=512, blank=True, null=True)
    social_credit_code = models.CharField(max_length=64, blank=True, null=True)
    legal_person = models.CharField(max_length=32, blank=True, null=True)
    status = models.SmallIntegerField()
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    corporation_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corporation'
        unique_together = (('name', 'is_delete'),)
        app_label = 'demoapp'


class CorporationContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    landline = models.CharField(max_length=512, blank=True, null=True)
    mobile = models.CharField(max_length=32)
    email = models.CharField(max_length=64, blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corporation_contacts'
        app_label = 'demoapp'


class CorporationContractConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    contract_name = models.CharField(max_length=64, blank=True, null=True)
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
        db_table = 'corporation_contract_config'
        app_label = 'demoapp'


class InstOutCodeSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(max_length=100)
    agent_bank_code = models.CharField(max_length=30)
    inst_out_code = models.CharField(max_length=30)
    inst_inner_code = models.CharField(max_length=30)
    direct_bank_code = models.CharField(max_length=30)
    ccpc_code = models.CharField(max_length=30)
    city_code = models.CharField(max_length=10)
    category_code = models.CharField(max_length=20)
    is_delete = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'inst_out_code_setting'
        app_label = 'demoapp'


class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    contract_id = models.BigIntegerField(unique=True)
    corp_id = models.BigIntegerField()
    corp_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_number = models.CharField(max_length=100, blank=True, null=True)
    social_credit_code = models.CharField(max_length=64)
    first_class = models.CharField(max_length=64, blank=True, null=True)
    first_class_id = models.IntegerField(blank=True, null=True)
    second_class_id = models.IntegerField(blank=True, null=True)
    second_class = models.CharField(max_length=64, blank=True, null=True)
    receipt_username = models.CharField(max_length=100, blank=True, null=True)
    receipt_telephone = models.CharField(max_length=16, blank=True, null=True)
    receipt_address = models.CharField(max_length=255, blank=True, null=True)
    receipt_logistics = models.CharField(max_length=255, blank=True, null=True)
    invoice_category = models.CharField(max_length=20, blank=True, null=True)
    invoice_type = models.CharField(max_length=20, blank=True, null=True)
    invoice_content = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)
    update_by = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'
        app_label = 'demoapp'


class InvoiceContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.BigIntegerField()
    invoice_content_number = models.CharField(max_length=50)
    invoice_content = models.CharField(max_length=100)
    tax_classification_code = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=12, decimal_places=6)
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    is_deleted = models.PositiveSmallIntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_content'
        unique_together = (('corp_id', 'invoice_content'),)
        app_label = 'demoapp'


class InvoiceSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    corp_id = models.PositiveBigIntegerField()
    corp_name = models.CharField(max_length=100)
    invoice_type = models.SmallIntegerField()
    invoice_machine_number = models.CharField(max_length=100)
    invoice_machine_tax_number = models.CharField(max_length=100)
    single_invoice_amount_limit = models.DecimalField(max_digits=12, decimal_places=2)
    annual_invoice_amount_limit = models.DecimalField(max_digits=12, decimal_places=2)
    annual_invoice_amount_used = models.DecimalField(max_digits=12, decimal_places=2)
    annual_invoice_amount_not_used = models.DecimalField(max_digits=12, decimal_places=2)
    print_limit = models.PositiveSmallIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=50)
    update_by = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    status = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_setting'
        app_label = 'demoapp'


class InvoiceTaxClassificationCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    tax_classification_code = models.CharField(max_length=50)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_tax_classification_code'
        app_label = 'demoapp'


class ProductData(models.Model):
    name = models.CharField(max_length=100)
    biz_category = models.CharField(max_length=20)
    individual_tax_rate = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    tax_rate_calculation_method = models.SmallIntegerField(blank=True, null=True)
    buy_service_charge_rate = models.CharField(max_length=64, blank=True, null=True)
    buy_vat_rate = models.CharField(max_length=64, blank=True, null=True)
    buy_service_fee_isnot_vat = models.CharField(max_length=64, blank=True, null=True)
    buy_algorithm = models.CharField(max_length=64, blank=True, null=True)
    sale_vendor = models.CharField(max_length=64, blank=True, null=True)
    sale_channel = models.CharField(max_length=64, blank=True, null=True)
    sale_contract_config = models.CharField(max_length=64, blank=True, null=True)
    sale_invitation_code = models.CharField(max_length=64, blank=True, null=True)
    sale_issue_attribute = models.CharField(max_length=64, blank=True, null=True)
    sale_manage_fee_rate = models.CharField(max_length=64, blank=True, null=True)
    sale_vat_rate = models.CharField(max_length=64, blank=True, null=True)
    sale_algorithm = models.CharField(max_length=64, blank=True, null=True)
    sale_manage_fee_isnot_vat = models.CharField(max_length=64, blank=True, null=True)
    sale_manage_fee_isnot_tax = models.CharField(max_length=64, blank=True, null=True)
    sale_entry_name = models.TextField(blank=True, null=True)
    sale_money_attribute = models.CharField(max_length=64, blank=True, null=True)
    extend_promotion_fee_rate = models.CharField(max_length=64, blank=True, null=True)
    extend_vat_rate = models.CharField(max_length=64, blank=True, null=True)
    extend_algorithm = models.CharField(max_length=64, blank=True, null=True)
    extend_promotion_fee_isnot_vat = models.CharField(max_length=64, blank=True, null=True)
    extend_billing_start_time = models.DateTimeField(blank=True, null=True)
    extend_billing_cycle_length = models.CharField(max_length=64, blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    product_setting = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    is_delete = models.SmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    extend_threshold_rate = models.CharField(max_length=64, blank=True, null=True)
    sale_task_type = models.CharField(max_length=2000, blank=True, null=True)
    extend_intermediary_fee_rate = models.CharField(max_length=64, blank=True, null=True)
    extend_intermediary_fee_includes_vat = models.SmallIntegerField(blank=True, null=True)
    outsource_manage_fee_rate = models.CharField(max_length=64, blank=True, null=True)
    outsource_vat_rate = models.CharField(max_length=64, blank=True, null=True)
    outsource_algorithm = models.CharField(max_length=64, blank=True, null=True)
    outsource_manage_fee_isnot_vat = models.CharField(max_length=64, blank=True, null=True)
    settlement_method = models.SmallIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_data'
        app_label = 'demoapp'


class ProductDataPackage(models.Model):
    name = models.CharField(max_length=100)
    contract_id = models.IntegerField()
    package_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_data_package'
        app_label = 'demoapp'


class ProductDataPackageDetail(models.Model):
    product_data_package_id = models.IntegerField(blank=True, null=True)
    product_data_id = models.IntegerField(blank=True, null=True)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    remark = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.SmallIntegerField()
    created_time = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    updated_time = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_data_package_detail'
        app_label = 'demoapp'


class ProductSetting(models.Model):
    name = models.CharField(max_length=100)
    biz_category = models.CharField(max_length=20)
    corporation_id = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    individual_tax_rate = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    tax_rate_calculation_method = models.SmallIntegerField(blank=True, null=True)
    buy_service_charge_rate = models.SmallIntegerField(blank=True, null=True)
    buy_vat_rate = models.SmallIntegerField(blank=True, null=True)
    buy_service_fee_isnot_vat = models.SmallIntegerField(blank=True, null=True)
    buy_algorithm = models.SmallIntegerField(blank=True, null=True)
    buy_settlement_method = models.SmallIntegerField(blank=True, null=True)
    sale_vendor = models.SmallIntegerField(blank=True, null=True)
    sale_channel = models.SmallIntegerField(blank=True, null=True)
    sale_contract_config = models.SmallIntegerField(blank=True, null=True)
    sale_invitation_code = models.SmallIntegerField(blank=True, null=True)
    sale_issue_attribute = models.SmallIntegerField(blank=True, null=True)
    sale_manage_fee_rate = models.SmallIntegerField(blank=True, null=True)
    sale_vat_rate = models.SmallIntegerField(blank=True, null=True)
    sale_algorithm = models.SmallIntegerField(blank=True, null=True)
    sale_manage_fee_isnot_vat = models.SmallIntegerField(blank=True, null=True)
    sale_manage_fee_isnot_tax = models.SmallIntegerField(blank=True, null=True)
    sale_entry_name = models.SmallIntegerField(blank=True, null=True)
    sale_money_attribute = models.SmallIntegerField(blank=True, null=True)
    sale_task_type = models.SmallIntegerField(blank=True, null=True)
    sale_settlement_method = models.SmallIntegerField(blank=True, null=True)
    extend_promotion_fee_rate = models.SmallIntegerField(blank=True, null=True)
    extend_vat_rate = models.SmallIntegerField(blank=True, null=True)
    extend_algorithm = models.SmallIntegerField(blank=True, null=True)
    extend_promotion_fee_isnot_vat = models.SmallIntegerField(blank=True, null=True)
    extend_billing_start_time = models.SmallIntegerField(blank=True, null=True)
    extend_billing_cycle_length = models.SmallIntegerField(blank=True, null=True)
    is_delete = models.SmallIntegerField()
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    extend_threshold_rate = models.SmallIntegerField(blank=True, null=True)
    extend_intermediary_fee_rate = models.SmallIntegerField(blank=True, null=True)
    extend_intermediary_fee_includes_vat = models.SmallIntegerField(blank=True, null=True)
    extend_settlement_method = models.SmallIntegerField(blank=True, null=True)
    outsource_manage_fee_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    outsource_vat_rate = models.SmallIntegerField(blank=True, null=True)
    outsource_algorithm = models.SmallIntegerField(blank=True, null=True)
    outsource_manage_fee_isnot_vat = models.SmallIntegerField(blank=True, null=True)
    outsource_settlement_method = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_setting'
        app_label = 'demoapp'


class TaskTypeInvoiceContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_type_id = models.BigIntegerField()
    invoice_content_id = models.BigIntegerField()
    remark = models.CharField(max_length=200, blank=True, null=True)
    create_corp_id = models.BigIntegerField()
    create_time = models.DateTimeField()
    create_by = models.CharField(max_length=50)
    update_time = models.DateTimeField(blank=True, null=True)
    update_by = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'task_type_invoice_content'
        unique_together = (('task_type_id', 'invoice_content_id', 'create_corp_id'),)
        app_label = 'demoapp'


class TaskTypeSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_delete = models.IntegerField()
    code = models.SmallIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    create_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_type_setting'
        app_label = 'demoapp'
