from audioop import reverse
from http import HTTPStatus
from django.test import TestCase, RequestFactory

from apps.accounts.views import AccountViewSet
from apps.accounts.models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from rest_framework.test import force_authenticate
from tests.factories import users, accounts

from django.http import HttpRequest, HttpResponse
from tests.fixtures import accounts

class AccountViewSetTest(TestCase):

    def setUp(self):
        # create one Account model object
        # account = Account.objects.create(id=1)
        accounts.make_objects()
        
        # create one superuser
        # user_model = get_user_model()
        # self.user = user_model.objects.create_superuser(email="test@user.com", password=r"***")
        self.factory = RequestFactory()
    
    def test_account_get_request(self):
        # import requests
        request = HttpRequest
        request.method = 'GET'
        # request.path = '/home/accounts/details'
        response = HttpResponse("")
        # response.data = 
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_account_authentication(self):
        account = Account.objects.first()
        # create instance of GET request
        request = self.factory.get('/home/accounts/details')
        # simulate logged-in user
        self.assertRaises(BaseException,  force_authenticate(request, user=account.user))
    
    def test_account_view_details(self):
        account = Account.objects.first()
        # create instance of GET request
        request = self.factory.get(path='/home/accounts/details')
        # simulate logged-in user
        force_authenticate(request, user=account.user)
        # Test view
        response = AccountViewSet.as_view({'get': 'retrieve'})(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_count_all_accounts(self):
        baseline = Account.objects.all()
        viewset = AccountViewSet()
        items = viewset.get_queryset()
        self.assertEqual(len(baseline), len(items))
    
    # def test_add_booking_to_account(self):


    # --- Rejected --- #
    # # Check that a user in incoming request gets associated with the account
    # # when an instance of AccountViewSet is being created
    # def test_create_instance(self):
    #     user_model = get_user_model()
    #     current_user = user_model.objects.get(id=1)
    #     account_viewset = AccountViewSet.get_object()
    #     self.assertEqual(current_user, )