from django.test import TestCase, RequestFactory
from apps.home import views
from http import HTTPStatus

class HomeTest(TestCase):
    
    def test_index(self):
        request = RequestFactory().get('/home')    
        response = views.index(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)