from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

# Create your views here.
class API_Root(APIView):
    def get(self, request, format=None):
        return Response({
            'home': reverse('index', request=request)
        })