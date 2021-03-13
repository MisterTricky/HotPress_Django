# Django Specific Imports
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
# Import predefined Values for Accounting models


from HotPressAdmin.Accounting.defines import TRANSACTION_STATUS_CHOICES, TRANSACTION_TYPE_CHOICES
from HotPressAdmin.HumanResources.models import Employee


class AccountYear(models.Model):
    name = models.CharField(max_length=(255), blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    slug = models.CharField(max_length=(255), blank=True)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    parent_type = models.ForeignKey('self', blank=True, null=True, default=None,
                                    related_name='prev_item',
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=(255), blank=True, null=True)
    slug = models.CharField(max_length=(255), blank=True, null=True)

    def __str__(self):
        return self.name


class Ledger(models.Model):
    code = models.CharField(max_length=(255), blank=True, null=True)
    account_type = models.ForeignKey(to=AccountType, blank=True, null=True,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=(255), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total_debit = models.DecimalField(verbose_name=("Total Debit"),
                                      default="0.00", max_digits=(12),
                                      decimal_places=(2))
    total_credit = models.DecimalField(verbose_name=("Total Credit"),
                                       default="0.00", max_digits=(12),
                                       decimal_places=(2))
    balance = models.DecimalField(verbose_name=("Balance"), default="0.00",
                                  max_digits=(12), decimal_places=(2))
    last_update_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=(32),
                                        choices=TRANSACTION_TYPE_CHOICES,
                                        blank=True)
    subject = models.CharField(max_length=(255), blank=True, null=True)
    ref_no = models.CharField(max_length=(255), blank=True, null=True)
    account_year = models.ForeignKey(to=AccountYear, blank=True, null=True,
                                     on_delete=models.CASCADE)
    voucher_no = models.CharField(max_length=(255), blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    post_status = models.CharField(max_length=(32),
                                   choices=TRANSACTION_STATUS_CHOICES)

    def __str__(self):
        return self.subject


class TransactionDetails(models.Model):
    transaction = models.ForeignKey(to=Transaction, blank=True, null=True, on_delete=models.CASCADE)
    ledger = models.ForeignKey(to=Ledger, blank=True, null=True, on_delete=models.CASCADE)
    account_holder = models.ForeignKey(to=Employee, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    vat_percentage = models.DecimalField(verbose_name=_('VAT %'), default='0.00', max_digits=12, decimal_places=2)
    tax_percentage = models.DecimalField(verbose_name=_('Tax %'), default='0.00', max_digits=12, decimal_places=2)
    debit = models.DecimalField(verbose_name=_('Debit'), default='0.00', max_digits=12, decimal_places=2)
    credit = models.DecimalField(verbose_name=_('Credit'), default='0.00', max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=255, blank=True, null=True)
    # quantity      = models.DecimalField(verbose_name="Quantity (Optional)",default="0.00",max_digits=12,
    #                                     decimal_places=2)
    # rate          = models.DecimalField(verbose_name="Rate (Optional)",default="0.00",max_digits=12,decimal_places=2)
    # amount        = models.DecimalField(verbose_name="Credit",default="0.00",max_digits=12,decimal_places=2)
    # entry_type     = models.CharField(max_length=32, choices=(('debit','debit'),('credit','credit')), blank=True)


class JournalEntry(models.Model):
    transaction = models.ForeignKey(to=Transaction, blank=True, null=True, on_delete=models.CASCADE)
    ref_no = models.CharField(max_length=255, blank=True, null=True, on_delete=models.CASCADE)
    debit = models.DecimalField(verbose_name=_('Debit'), default="0.00", max_digits=12, decimal_places=2)
    credit = models.DecimalField(verbose_name=_('Credit'), default="0.00", max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=255, blank=True, null=True, on_delete=models.CASCADE)
    entry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ref_no + " " + " " + self.transaction.subject
