from django.contrib import admin
from .models import UserAccount, Transactions

admin.site.register(UserAccount)
admin.site.register(Transactions)
