from ast import NodeTransformer
from tracemalloc import get_object_traceback
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from bookings.models import Member
from bookings.serializers import MemberSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET', 'POST'])
class MemberList(APIView):

    def get(self, request, format=None):
        member_list = Member.objects.all()
        serializer = MemberSerializer(member_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):     
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)

class MemberDetail(APIView):
    # def detail(request, member_id):
    #     return HttpResponse("You just retrieved Member ID: %s." % member_id )

    def get_object(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # data = JSONParser().parse(request)
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)