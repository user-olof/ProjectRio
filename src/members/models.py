from django.db import models
from accounts.models import Account

# Create your models here.
# Member model is independent of EventsAndClasses
class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=8)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    last_login = models.DateTimeField('Last login')
    account = models.ForeignKey(Account, related_name="account", on_delete=models.CASCADE)

    class Meta:
        unique_together = ['account', 'email']
        ordering = ['created']

 
    def __str__(self) -> str:
        return '%s %s' % (self.first_name, self.surname)