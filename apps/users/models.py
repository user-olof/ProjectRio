from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from rioacademy.apps.users.managers import CustomUserManager
from apps.users.managers import CustomUserManager
from django.utils import timezone

def get_default_user():
    """ returns user object using the defaults """
    return CustomUser.objects.get_or_create()

def get_default_user_id():
    """ returns the id of the default user """
    user = get_default_user()
    return user[0]

class CustomUser(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)

    username = None
    email = models.EmailField(_('email address'), unique=True, null=True, max_length=200, default='empty')

    
    # email = models.CharField(max_length=200)
    title = models.CharField(max_length=8, default='-')
    first_name = models.CharField(max_length=200, default='-')
    surname = models.CharField(max_length=200, default='-')
    level = models.CharField(max_length=200, default='Beginner')
    last_login = models.DateTimeField('last_login', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

