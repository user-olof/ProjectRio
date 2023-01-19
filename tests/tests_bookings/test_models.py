from django.test import TestCase, RequestFactory, Client
from apps.bookings.models import Booking
from apps.bookings.serializers import BookingSerializer
from apps.bookings.views import BookingViewSet
from apps.accounts.models import Account
# from tests.fixtures import bookings
from tests.fixtures import bookings, accounts
from django.urls import reverse, path



class BookingsTest(TestCase):

    @classmethod
    def setUp(self):
        bookings.make_objects()
        accounts.make_objects()
        self.factory = RequestFactory()

    def test_event_is_test_lesson(self):
        booking = Booking.objects.first()
        self.assertEqual(booking.event, "test_lesson")

    def test_account_is_default_test_account(self):
        account = Account.objects.first()
        self.assertEqual(account.name, "default_test_account")

    def test_seralizer_data_is_valid(self):
        request = self.factory.get('/bookings/details')
        response = BookingViewSet.as_view({
            'get': 'retrieve'
            })(request, pk=1)
        # get the first element in OrderedDict of output 
        # wrap output in a list and then get the third element, corresponding to 'event' in Booking
        items = dict(response.data.items())
        event = items['event']
        self.assertEqual(event, 'test_lesson')

    def test_booking_url(self):
        c = Client()
        response = c.get('/home/bookings/')
        self.assertEqual(response.status_code, 200)

    def test_booking_detail_url(self):
        request = self.factory.get('/bookings/details')
        response = BookingViewSet.as_view({
            'get': 'retrieve'
            })(request, pk=1)
        self.assertEqual(response.status_code, 200)
    
    def test_booking_is_linked_to_default_test_account(self):
        request = self.factory.get('/bookings/details')
        response = BookingViewSet.as_view({
            'get': 'retrieve'
            })(request, pk=2)
        # get the first element in OrderedDict of output 
        # wrap output in a list and then get the third element, corresponding to 'account' in Booking
        items = dict(response.data.items())
        account = items['account']
        url_regex = r'home/accounts/[0-9]'
        self.assertRegex(account, url_regex)

