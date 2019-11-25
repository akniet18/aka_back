from django.db import models
from datetime import datetime


def upload_path(filename):
    folder_name = f"{datetime.today().strftime('%d_%m_%Y')}/{filename}"

    return folder_name

class Uploads(models.Model):
	file = models.FileField(upload_to=upload_path, blank=True, null=True)

