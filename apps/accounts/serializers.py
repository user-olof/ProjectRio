from rest_framework import serializers

# from members.models import Member
from apps.accounts.models import Account
# from apps.users.models import CustomUser

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'created', 'name', 'member', 'user']
