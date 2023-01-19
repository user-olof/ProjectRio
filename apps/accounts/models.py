from django.db import models

from apps.users.models import CustomUser, get_default_user_id


def get_default_account():
    """ returns an account object using the defaults """
    return Account.objects.get_or_create()

def get_default_account_id() -> int:
    """ returns id of account default object """
    account = get_default_account()
    return account[0].pk

# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=25, default='empty')
    # owner = models.ForeignKey(CustomUser, null=True, blank=True, related_name="users", on_delete=models.CASCADE)
    # owner = models.ForeignKey(CustomUser, related_name='email', default=None, on_delete=models.CASCADE, null=True, blank=True)
    # "an account has an owner"
    member = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=get_default_user_id, unique=False)
    # user_id = models.IntegerField(null=False)

    def get_label(self, field_name):
        return Account._meta.get_field(field_name).verbose_name

    class Meta:
        ordering = ['created']
        # fields = ['created', 'user_name']

    def __str__(self):
        return self.name
    
