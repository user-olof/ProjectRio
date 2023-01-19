import factory
# from apps.users.models import CustomUser, CustomUserManager
from django.contrib.auth import get_user_model
from django.utils import timezone
import pytz
import datetime
# from django.contrib.auth import get_user_model

# class CustomUserManagerFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = CustomUserManager

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('email', 'title', 'first_name', 'surname', 'level', 'last_login', 'password')

    email = "john.doe@user.com"
    title = 'Mr'
    first_name = 'John'
    surname = 'Doe'
    level = 'Beginner'
    last_login = datetime.datetime(2000, 1, 1, tzinfo=pytz.UTC) 
    password = "***"
    
    # username = "foo"
    # email = "normal@user.com"