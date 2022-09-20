from ast import NodeTransformer
import imp
from tracemalloc import get_object_traceback
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import EventsAndClasses
from .serializers import EventsAndClassesSerializer
from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly



# from django.contrib.auth.models import User
# from users.models import CustomUser


class EventsAndClassesList(generics.ListCreateAPIView):
    queryset = EventsAndClasses.objects.all()
    serializer_class = EventsAndClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventsAndClassesDetail(generics.RetrieveUpdateAPIView):
    queryset = EventsAndClasses.objects.all()
    serializer_class = EventsAndClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventsAndClassesName(generics.GenericAPIView):
    queryset = EventsAndClasses.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        member = self.get_object()
        return Response(member.name)


