from django.db import models

# from members.models import Member


# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=25)
    # owner = models.ForeignKey(Member, related_name="members", on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.user_name
    
