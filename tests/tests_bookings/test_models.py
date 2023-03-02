from django.test import TestCase, RequestFactory
from apps.bookings.models import Booking
# from apps.bookings.serializers import BookingSerializer
# from apps.bookings.views import BookingViewSet
from apps.accounts.models import Account
# from tests.fixtures import bookings
from tests.fixtures import bookings, accounts
# from django.urls import reverse, path



class BookingsTest(TestCase):

    @classmethod
    def setUp(self):
        bookings.make_objects()


    def test_event_is_test_lesson(self):
        booking = Booking.objects.first()
        self.assertEqual(booking.event, "test_lesson")




    

