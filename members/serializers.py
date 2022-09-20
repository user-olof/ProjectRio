from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Member
        fields = ['title', 'email', 'first_name', 'surname', 'level', 'last_login', 'owner']
