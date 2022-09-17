from django.db import models

from events_and_classes.models import EventsAndClasses, Member


# Create your models here.

class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #Each booking is related to a single event, one-to-one 
    event = models.CharField(max_length=200)
    # event = models.ForeignKey(EventsAndClasses, on_delete=models.CASCADE, primary_key=True)
    #Each booking is related to a single member, one-to-one
    member = models.CharField(max_length=200)
    # member = models.ForeignKey(Member, on_delete=models.CASCADE, unique=True)

    class Meta:
        ordering = ['created']