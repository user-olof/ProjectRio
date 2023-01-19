import factory
from . import users
from apps.accounts.models import Account

    # objects = factory.SubFactory(CustomUserManagerFactory)


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = "default_test_account"
    member = True
    user = factory.SubFactory(users.CustomUserFactory)
 
    
