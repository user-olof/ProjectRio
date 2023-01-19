from django.contrib import admin
from apps.accounts.models import Account

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields = ('created', 'name')
    list_display = ('created', 'name')
    search_fields = ('created', 'name')