from django.db import models
from apps.accounts.models import Account
from apps.events_and_classes.models import EventsAndClasses
# from apps.users.models import CustomUser, get_default_user_id
# from events_and_classes.models import EventsAndClasses


# Create your models here.

class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #Each booking is related to a single event, one-to-one 
    # event = models.CharField(max_length=200)
    event = models.ForeignKey(EventsAndClasses, on_delete=models.CASCADE, default=0)
    #Each booking is related to a single account, one-to-one
    # account = models.OneToOneField(Account, on_delete=models.CASCADE, default=0)

    #Each account is related to many bookings, one-to-many
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=0)
    
    class Meta:
        ordering = ['created']


    # saved = False

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # owner = models.ForeignKey('users.CustomUser', related_name='booking', on_delete=models.CASCADE)
    # owner_textfield = models.TextField()
    # saved = False

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)