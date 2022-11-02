from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from dataclasses import fields

from .models import EventsAndClasses

class EventsAndClassesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventsAndClasses
        fields = ['url', 'id', 'name', 'time_length', 'next_event', 'frequency', 'address', 'max_participants']



