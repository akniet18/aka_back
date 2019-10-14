from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('id', 'title', 'text', 'views', 'author', 'favorite')
		read_only_fields  = ('user', 'author', 'favorite', 'views')


class addFavSer(serializers.Serializer):
	id = serializers.IntegerField()