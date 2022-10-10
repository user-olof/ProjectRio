from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import Account

class AccountsTest(TestCase):

    def create_account(self, user_name='this is a test'):
        return Account.objects.create(user_name=user_name)

    def test_account_creation(self):
        acct = self.create_account()
        self.assertTrue(isinstance(acct, Account))
        # self.assertEqual(acct.__unicode__(), acct.user_name)


# class UserLoginTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create_user(email='test@user.com', password='123')
#         self.user.save()

#     def test_correct_login(self):
#         # unit test
#         # assert

#     def test_if_password_incorrect_then_cant_login(self):

    
