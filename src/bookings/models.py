from django.db import models

# from events_and_classes.models import EventsAndClasses


# Create your models here.

class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #Each booking is related to a single event, one-to-one 
    event = models.CharField(max_length=200)
    # event = models.ForeignKey(EventsAndClasses, on_delete=models.CASCADE, primary_key=True)
    #Each booking is related to a single member, one-to-one
    member = models.CharField(max_length=200)
    # member = models.ForeignKey(Member, on_delete=models.CASCADE, unique=True)
    # owner = models.ForeignKey('users.CustomUser', related_name='bookings', on_delete=models.CASCADE, default=0)
    # owner_textfield = models.TextField(default='(Empty)')

    class Meta:
        ordering = ['created']


    # saved = False

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    owner = models.ForeignKey('users.CustomUser', related_name='booking', on_delete=models.CASCADE)
    owner_textfield = models.TextField()
    saved = False

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)