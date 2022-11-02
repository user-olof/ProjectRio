from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    # accounts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='member-detail')

    class Meta:
        model = Member
        fields = ['url', 'id', 'title', 'email', 'first_name', 'surname', 'level', 'last_login']
