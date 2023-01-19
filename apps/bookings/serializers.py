from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# from dataclasses import dataclass
from .models import Booking
from apps.accounts.models import Account


class BookingSerializer(serializers.HyperlinkedModelSerializer)  :
    # account = serializers.HyperlinkedRelatedField(view_name='apps.account:account-detail', lookup_field='name', many=True, read_only=True)
    account = serializers.HyperlinkedIdentityField(view_name='account-detail')

    class Meta:
        model = Booking
        fields = ['url', 'id', 'event', 'account']


    def __repr__(self):
        return 







