
from tracemalloc import get_object_traceback
from django.shortcuts import render

# Create your views here.
from .models import EventsAndClasses
from .serializers import EventsAndClassesSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly


class EventsAndClassesViewSet(viewsets.ModelViewSet):
    queryset = EventsAndClasses.objects.all()
    serializer_class = EventsAndClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




