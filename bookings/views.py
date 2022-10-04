from django.shortcuts import render
from rest_framework import viewsets, permissions, renderers
from rest_framework.decorators import action
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response


from django.shortcuts import get_object_or_404


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #This saves that the User is also the owner 
    #of the created member list. All member lists
    #will be owned by the admin
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def book(self, request, *args, **kwargs):
        booking = self.get_object()
        return Response(booking.event)







    # def create(self, request):
    #     dto = self._build_dto_from_validated_data(request)

    #     booking_service = BookingService()
    #     try:
    #         booking_service.book(dto)
    #     except BookingFailure:
    #         return JsonResponse()

    
#     def _build_dto_from_validated_data(self, request) -> dict:
#         serializer = BookingSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
#         return BookingDto(
#             event=data["event"],
#             member=data["member"]
#         )