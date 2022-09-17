from ast import NodeTransformer
import imp
from tracemalloc import get_object_traceback
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import EventsAndClasses, Member
from .serializers import EventsAndClassesSerializer, MemberSerializer
from rest_framework import generics

from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# from django.contrib.auth.models import User
from users.models import CustomUser


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'events_and_classes': reverse('events_and_classes-list', request=request, format=format)
    })

class EventsAndClassesList(generics.ListCreateAPIView):
    queryset = EventsAndClasses.objects.all()
    serializer_class = EventsAndClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventsAndClassesDetail(generics.RetrieveUpdateAPIView):
    queryset = EventsAndClasses.objects.all()
    serializer_class = EventsAndClassesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #This saves that the User is also the owner 
    #of the created member list. All member lists
    #will be owned by the admin
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MemberView(generics.GenericAPIView):
    queryset = Member.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        member = self.get_object()
        return Response(member.email)
