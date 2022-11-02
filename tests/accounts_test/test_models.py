from warnings import catch_warnings
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Account
# import pdb

class AccountsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # pdb.Pdb(skip=['django.*']).set_trace()
        Account.objects.create(id=1)

    def test_account_creation(self):
        try:
            account = Account.objects.get(id=1)
        except BaseException:
            account = None
        self.assertTrue(isinstance(account, Account))
    
    def test_user_name_label(self):
        account = Account.objects.get(id=1)
        label = account.get_label(r'user_name')
        self.assertEqual(label, 'user name')
        # self.assertEqual(acct.__unicode__(), acct.user_name)

    def test_user_name_str(self):
        account = Account.objects.get(id=1)
        self.assertEqual(account.__str__(), 'Mr Test')


# class UserLoginTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create_user(email='test@user.com', password='123')
#         self.user.save()

#     def test_correct_login(self):
#         # unit test
#         # assert

#     def test_if_password_incorrect_then_cant_login(self):

    
