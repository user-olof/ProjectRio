from django.db import models

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

    class Meta:
        ordering = ['created']

 
    def __str__(self) -> str:
        return self.first_name + " " + self.surname