from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey


class Article(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
	title = models.CharField(max_length = 150)
	views = models.IntegerField(blank=True, null = True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	text = RichTextUploadingField()
	favorite = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='fav', blank=True)
	tags = TaggableManager()
	is_blog = models.BooleanField(default=False)
	is_q = models.BooleanField(default=False)
	is_news = models.BooleanField(default=False)

	def comment(self):
		return self.comment.all()

	def __str__(self):
		return self.title


class Comment(MPTTModel):
	text = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,related_name='comment_author')
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
	parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'author: {}, article: {}'.format(self.author, self.article)

	def children(self):
		return self.child.all()


