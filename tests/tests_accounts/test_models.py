# from warnings import catch_warnings
from django.test import TestCase
# from unittest import TestCase
from apps.accounts.models import Account
# from tests.factories.accounts import AccountFactory
from tests.fixtures import accounts
from apps.users.models import CustomUser
# import pdb

class AccountsTest(TestCase):

    @classmethod
    def setUp(self):
        accounts.make_objects()

    def test_account_is_default_test_account(self):
        account = Account.objects.first()
        self.assertEqual(account.name, "default_test_account")

    def test_count_all_accounts_to_4(self):
        accounts = Account.objects.all()
        assert len(accounts) == 4
       
    def test_str_returning_default_test_account(self):
        account = Account.objects.first()
        assert account.__str__() == 'default_test_account'

    def test_user_email(self):
        account = Account.objects.first()
        assert account.user.email == "john.doe@user.com"

    def test_foreign_key_user(self):
        # get the John Doe user
        user = CustomUser.objects.get(email="john.doe@user.com")
        # create instance of the new account and link it to the user
        instance = Account(name='JD', member=True, user=user)
        instance.save()
        # get the account object 
        account = Account.objects.get(name='JD')
        assert account.user.email == "john.doe@user.com"
        # account_user = CustomUser(email='test@test.com')
        


# class UserLoginTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create_user(email='test@user.com', password='123')
#         self.user.save()

#     def test_correct_login(self):
#         # unit test
#         # assert

#     def test_if_password_incorrect_then_cant_login(self):

    
