from rest_framework import serializers
from .models import *
from users.serializers import *


class CommSerilaizer(serializers.ModelSerializer):
	author = UserDSerializer()
	class Meta:
		model = Comment
		fields = "__all__"
		read_only_fields  = ('author', 'date')


		
class StringListField(serializers.ListField): # get from http://www.django-rest-framework.org/api-guide/fields/#listfield
    child = serializers.CharField()

    def to_representation(self, data):
        return ' '.join(data.values_list('name', flat=True))


class ArticleSerializer(serializers.ModelSerializer):
	tags = StringListField()
	author = UserDSerializer(read_only=True)
	class Meta:
		model = Article
		fields = ('id', 'title', 'text', 'views', 'author', 'favorite', 'tags', 'comment', 'date', "is_blog", 'is_q', 'is_news')
		read_only_fields  = ('author', 'favorite', 'views', 'comment')



class TagSerializer(serializers.Serializer):
	tag = serializers.CharField()	



class addFavSer(serializers.Serializer):
	id = serializers.IntegerField()



class CommentSerilaizer(serializers.ModelSerializer):
	author = UserDSerializer(read_only=True)
	class Meta:
		model = Comment
		fields = "__all__"
		read_only_fields  = ('author', 'date')