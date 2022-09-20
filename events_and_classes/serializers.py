from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from dataclasses import fields

from .models import EventsAndClasses




# class MemberSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, max_length=200)
#     first_name = serializers.CharField(required=True, max_length=200)
#     surname = serializers.CharField(required=True)
#     level = serializers.CharField(required=False, allow_blank=True, max_length=200)
#     last_login = serializers.DateTimeField(required=True)

#     def create(self, validated_data):
#         return Member.objects.create(**validated_data)

#     def update(self, validated_data, instance: Member):
#         instance.title = validated_data.get('title', instance.title)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.surname = validated_data.get('surname', instance.surname)
#         instance.level = validated_data.get('level', instance.level)
#         instance.last_login = validated_data.get('last_login', instance.last_login)
#         instance.save()
#         return instance

class EventsAndClassesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventsAndClasses
        fields = ['name', 'time_length', 'next_event', 'frequency', 'address', 'max_participants']



