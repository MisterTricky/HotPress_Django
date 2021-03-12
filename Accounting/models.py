# Django Specific Imports
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
# Import predefined Values for Accounting models
from Accounting.defines import *

class AccountYear(models.Model):
    name = models.CharField(max_length=(255), blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    slug = models.CharField(max_length=(255), blank=True)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    parent_type = models.ForeignKey('self', blank=True, null =True, default=None,
                                    related_name='prev_item',
                                    on_delete=models.CASCADE)
    name        = models.CharField(max_length=(255), blank=True, null=True)
    slug        = models.CharField(max_length=(255), blank=True, null=True)

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

class Transaction(BaseModel):
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

# class TransactionDetails(models.Model):
