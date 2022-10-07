from rest_framework import serializers

# from members.models import Member
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    member = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='member-detail')

    class Meta:
        model = Account
        fields = ['url', 'id', 'user_name', 'member']
