from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.BookingsList.as_view(), name="bookings_list"),
    path('bookings/<int:pk>/', views.BookingsDetail.as_view(), name="bookings_detail")
]