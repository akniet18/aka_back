from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import random

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import permission_classes
import random
from django.contrib.auth import (login as django_login,
                                 logout as django_logout)
from rest_auth.utils import jwt_encode, default_create_token as create_token
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class Register(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = RegUsers(data = request.data)
		if s.is_valid():
			username = s.validated_data['username']
			email = s.validated_data['email']
			password = s.validated_data['password']
			if User.objects.filter(username=username, email=email).exists():
				return Response({'status': 'User already exists'})
			else: 
				user = User.objects.create(
					username = username,
					email = email,
				)
				user.set_password(password)
				user.save()
				return Response({'status': 'ok'})
		else:
			return Response(s.errors)


class Login(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = LoginUsers(data = request.data)
		if s.is_valid():
			username_or_email = s.validated_data['username_or_email']
			password = s.validated_data['password']
			if '@' in username_or_email:
				if User.objects.filter(email=username_or_email).exists():
					u = User.objects.get(email=username_or_email)
					if u.check_password(password):
						django_login(request, u)
						if Token.objects.filter(user=u).exists():
							token = Token.objects.get(user=u)
						else:
							token = Token.objects.create(user=u)
						return Response({'token': token.key, 'uid': u.id})
					else:
						return Response({'status': 'username or password wrong'})
				else:
					return Response({'status': 'username or password wrong'})
			else:
				if User.objects.filter(username=username_or_email).exists():
					u = User.objects.get(username=username_or_email)
					if u.check_password(password):
						django_login(request, u)
						if Token.objects.filter(user=u).exists():
							token = Token.objects.get(user=u)
						else:
							token = Token.objects.create(user=u)
						return Response({'token': token.key, 'uid': u.id})
					else:
						return Response({'status': 'username or password wrong'})
				else:
					return Response({'status': 'username or password wrong'})
		else:
			return Response(s.errors)


class getUser(RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = UserSerializer
	queryset = User.objects.all()



