from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from dataclasses import dataclass
from .models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Booking
        fields = ['url', 'id', 'event', 'member']








