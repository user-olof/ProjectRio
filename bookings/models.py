from django.db import models
import datetime
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=8)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    last_login = models.DateTimeField('Last login')

    class Meta:
        ordering = ['created']

    owner = models.ForeignKey('users.CustomUser', related_name='members', on_delete=models.CASCADE)
    owner_textfield = models.TextField()
    saved = False

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
        

    def __str__(self) -> str:
        return self.first_name + " " + self.surname

# class User(models.Model):
#     username = models.CharField(max_length=200)
    

class Event(models.Model):
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

class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #Each booking is related to a single event, one-to-one 
    event = models.ForeignKey(Event, on_delete=models.CASCADE, primary_key=True)
    #Each booking is related to a single member, one-to-one
    member = models.ForeignKey(Member, on_delete=models.CASCADE, unique=True)

    class Meta:
        ordering = ['created']