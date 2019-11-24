from rest_framework import serializers
from .models import *
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from users.serializers import *


class CommSerilaizer(serializers.ModelSerializer):
	author = UserDSerializer()
	class Meta:
		model = Comment
		fields = "__all__"
		read_only_fields  = ('author', 'date')



class ArticleSerializer(serializers.ModelSerializer):
	tags = TagListSerializerField()
	comment = CommSerilaizer(many=True, read_only=True)
	author = UserDSerializer()
	class Meta:
		model = Article
		fields = ('id', 'title', 'text', 'views', 'author', 'favorite', 'tags', 'comment', 'date')
		read_only_fields  = ('author', 'favorite', 'views')



class TagSerializer(serializers.Serializer):
	tag = serializers.CharField()	



class addFavSer(serializers.Serializer):
	id = serializers.IntegerField()



class CommentSerilaizer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = "__all__"
		read_only_fields  = ('author', 'date')