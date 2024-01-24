# models.py w aplikacji profiles

from django.db import models
from accounts.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pesel = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email
