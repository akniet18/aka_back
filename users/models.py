from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to = 'media/avatar', blank=True, null=True)

