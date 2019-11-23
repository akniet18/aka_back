from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class Article(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length = 150)
	views = models.IntegerField(blank=True, null = True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	text = RichTextUploadingField()
	favorite = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='fav', blank=True)
	tags = TaggableManager()

	def comment(self):
		return self.comment.all()

	def __str__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
	parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'author: {}, article: {}'.format(self.author, self.article)


