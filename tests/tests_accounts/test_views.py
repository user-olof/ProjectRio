from audioop import reverse
from http import HTTPStatus
from django.test import TestCase, RequestFactory

from rioacademy.apps.accounts.views import AccountViewSet
from rioacademy.apps.accounts.models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from rest_framework.test import force_authenticate

class AccountViewSetTest(TestCase):

    def setUp(self):
        # create one Account model object
        account = Account.objects.create(id=1)
        # create one superuser
        user_model = get_user_model()
        self.user = user_model.objects.create_superuser(email="test@user.com", password=r"***")
        # create RequestFactory object
        self.factory = RequestFactory()
       

    
    def test_account_view_creation(self):
        # create instance of GET request
        request = self.factory.get('/accounts/details')
        # simulate logged-in user
        force_authenticate(request, user=self.user)
        # Test view
        response = AccountViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)


    # --- Rejected --- #
    # # Check that a user in incoming request gets associated with the account
    # # when an instance of AccountViewSet is being created
    # def test_create_instance(self):
    #     user_model = get_user_model()
    #     current_user = user_model.objects.get(id=1)
    #     account_viewset = AccountViewSet.get_object()
    #     self.assertEqual(current_user, )