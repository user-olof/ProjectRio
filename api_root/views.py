from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'home': reverse('index', request=request)
        # 'users': reverse('user-list', request=request, format=format),
        # 'events_and_classes': reverse('events_and_classes-list', request=request, format=format)
    })