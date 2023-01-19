from rest_framework import serializers
from .models import CustomUser
from bookings.models import Booking

# class UserSerializer(serializers.HyperlinkedModelSerializer):
    # bookings = serializers.HyperlinkedRelatedField(many=True, view_name='booking-detail', read_only=True)
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'title', 'first_name', 'surname', 'level', 'last_login']