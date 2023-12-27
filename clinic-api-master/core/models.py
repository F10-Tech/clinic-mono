from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True, blank=True, null=False, default=0)
    otp = models.CharField(max_length=6, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email



    


