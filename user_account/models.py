from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    number = models.IntegerField()
    agency = models.IntegerField(default=1, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.number} - {self.agency}'

    def add_money(self, value):
        self.balance = self.balance + value

    def remove_money(self, value):
        value = Decimal(value)
        if self.balance > value:
            self.balance = self.balance - value
            return True
        return False

        
class Transactions(models.Model):
    type_transaction_choices = (
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT')
    )
    datetime = models.DateField(auto_now_add=True, editable=False)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    log_extract = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    type = models.CharField(max_length=6, choices=type_transaction_choices, editable=False)
    description = models.TextField(max_length=155)
    account = models.ForeignKey(UserAccount, related_name='transactions', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.account.__str__()
