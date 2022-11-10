from django.db import models
import datetime

# this app main model is EventsAndClasses 
class EventsAndClasses(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    time_length = models.IntegerField()
    next_event = models.DateTimeField()
    frequency = models.CharField(max_length=8)
    address = models.CharField(max_length=200)
    max_participants = models.IntegerField()

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return self.name

    def is_today(self):
        todays_date = datetime.now()
        if todays_date == self.next_event:
            return True
        return False



# class User(models.Model):
#     username = models.CharField(max_length=200)
    



