from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", include("events_and_classes.urls")),
    path("", include("members.urls")),
    path("", include("bookings.urls")), 
    path("", include("accounts.urls")),
]