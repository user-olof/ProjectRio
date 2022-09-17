from rest_framework import serializers
from .models import CustomUser
from bookings.models import Booking

class UserSerializer(serializers.ModelSerializer):
    bookings = serializers.PrimaryKeyRelatedField(many=True, queryset=Booking.objects.all())

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'members', 'bookings']