from django.test import TestCase, RequestFactory
from apps.api_root.views import API_Root
from http import HTTPStatus

class ApiRootTest(TestCase):

    def test_api_root(self):
        request = RequestFactory().get('/')
        response = API_Root.get(request, None) 
        self.assertEqual(response.status_code, HTTPStatus.OK)