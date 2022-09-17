from django.shortcuts import render
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingsList(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingsDetail(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer