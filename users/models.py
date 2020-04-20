from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.username}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"
    return folder_name


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to = user_photos_dir, blank=True, null=True, default="default/user.svg")
    about = models.TextField(blank=True, null=True)

