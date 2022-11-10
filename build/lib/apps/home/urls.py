from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", include("rioacademy.apps.events_and_classes.urls")),
    path("", include("rioacademy.apps.members.urls")),
    path("", include("rioacademy.apps.bookings.urls")), 
    path("", include("rioacademy.apps.accounts.urls")),
]