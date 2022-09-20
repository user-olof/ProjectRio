from django.shortcuts import render

from .models import Member
from .serializers import MemberSerializer
from rest_framework import generics, permissions, renderers
from rest_framework.response import Response

# Create your views here.

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