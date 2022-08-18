from ast import NodeTransformer
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
def bookings_list(request, format=None):
    # return HttpResponse("RioAcedemy: Booking")
    if request.method == 'GET':
        member_list = Member.objects.all()
        serializer = MemberSerializer(member_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status.HTTP_400_BAD_REQUEST)


def detail(request, member_id):
    return HttpResponse("You just retrieved Member ID: %s." % member_id )

@api_view(['GET', 'PUT', 'DELETE'])
def bookings_detail(request, pk, format=None):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)