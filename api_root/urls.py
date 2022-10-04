from django.urls import path
from . import views

urlpatterns = [
    path('', views.API_Root.as_view())
]