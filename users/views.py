from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
# class UserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer