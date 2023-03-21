from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model
from apps.bookings.views import BookingViewSet
from tests.fixtures import bookings
from apps.bookings.models import Booking
from apps.accounts.models import Account
from apps.events_and_classes.models import EventsAndClasses
from datetime import datetime 
import pytz

class BookingViewSetTest(TestCase):

    def setUp(self):
        bookings.make_objects()
        self.factory = RequestFactory()

    def test_booking_event_equal_test_lesson(self):
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
        # get the default user
        user = Booking.objects.first()
        request = self.factory.get('/bookings/details')
        response = BookingViewSet.as_view({
            'get': 'retrieve'
            })(request, pk=2)
        # get the first element in OrderedDict of output 
        # wrap output in a list and then get the third element, corresponding to 'account' in Booking
        items = dict(response.data.items())
        account = items['account']
        url_regex = r'[0-9]'
        self.assertRegex(str(account), url_regex)  

    def test_create_new_booking(self):
        account = Account.objects.first()
        event = EventsAndClasses.objects.first()
        new_booking, created = Booking.objects.get_or_create(event=event, account = account)
        self.assertEqual(new_booking.event.name, "Test lesson" )
    
    
    # def test_post_one_booking_by_default_user(self):
    #     user = 
    #     data = {'event':'xxx'}
    #     request = self.factory.post('/booking/create', data, content_type='application/json')
    #     response = BookingViewSet.as_view({'post': 'create'})(request)
    #     self.assertEqual(response.status_code, 302)