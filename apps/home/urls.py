from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", include("apps.events_and_classes.urls")),
    path("", include("apps.bookings.urls")), 
    path("", include("apps.accounts.urls")),
]