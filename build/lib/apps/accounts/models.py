from django.db import models

from rioacademy.apps.users.models import CustomUser


# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=25)
    owner = models.ForeignKey(CustomUser, null=True, blank=True, related_name="users", on_delete=models.CASCADE)

    def get_label(self, field_name):
        return Account._meta.get_field(field_name).verbose_name

    class Meta:
        ordering = ['created']
        # fields = ['created', 'user_name']

    def __str__(self):
        return self.user_name
    
