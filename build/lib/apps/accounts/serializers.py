from rest_framework import serializers

# from members.models import Member
from rioacademy.apps.accounts.models import Account

class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='user-detail')

    class Meta:
        model = Account
        fields = ['url', 'id', 'user_name', 'owner']
