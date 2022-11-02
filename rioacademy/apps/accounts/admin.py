from django.contrib import admin
from rioacademy.apps.accounts.models import Account

# Register your models here.
@admin.register(Account)
class Account(admin.ModelAdmin):
    fields = ('created', 'user_name')
    list_display = ('created', 'user_name')
    serach_fields = ('created', 'user_name')