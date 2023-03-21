from django.test import RequestFactory
import unittest
from unittest.mock import patch
from apps.bookings.views import BookingViewSet
from http import HTTPStatus 


class TestBookingsMocking(unittest.TestCase):
    def test_mock_view_