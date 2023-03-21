from django.test import RequestFactory
import unittest
from unittest.mock import patch
from apps.accounts.views import AccountViewSet
from http import HTTPStatus   


class TestAccountsMocking(unittest.TestCase):

    @patch('apps.accounts.views.AccountViewSet.retrieve')
    def test_mock_view_details(self, mock_view_details):     
        mock_view_details.return_value.status_code = 200

        request = RequestFactory()
        r = request.get('/home/accounts/detail')
        response = mock_view_details(r)
        
        self.assertEqual(mock_view_details.called, True)
        self.assertEqual(response.status_code, mock_view_details.return_value.status_code)
    
    def test_mock_view_list(self):
        with patch('apps.accounts.views.AccountViewSet.list') as mock_view:
            mock_view.return_value.status_code = 200

            request = RequestFactory()
            r = request.get('/home/accounts/list')
            response = mock_view(r)

        self.assertEqual(mock_view.called, True)
        self.assertEqual(response.status_code, mock_view.return_value.status_code)       

    
    