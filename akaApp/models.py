from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length = 150)
	views = models.IntegerField(blank=True, null = True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	text = RichTextUploadingField()
	favorite = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='fav', blank=True)

	def __str__(self):
		return self.title

