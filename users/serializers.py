from rest_framework import serializers
from .models import *


class RegUsers(serializers.Serializer):
	username = serializers.CharField(max_length=15)
	email = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=20)


class LoginUsers(serializers.Serializer):
	username_or_email = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=20)


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id' ,'username', 'email', 'birth_date', 'first_name', 'last_name', 'avatar', 'about')



class UserDSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id' ,'username', 'email', 'avatar')