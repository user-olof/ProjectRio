# from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from dataclasses import dataclass
from .models import Booking
# from apps.accounts.models import Account


class BookingSerializer(serializers.ModelSerializer)  :

    # THIS LINE WORKS:
    # account = serializers.HyperlinkedIdentityField(view_name='account-detail')

    class Meta:
        model = Booking
        fields = ['url', 'id', 'created', 'event', 'account']


    def __repr__(self):
        return 







