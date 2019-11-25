from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import filters


User = get_user_model()


class UploadsView(viewsets.ModelViewSet):
	queryset = Uploads.objects.all()
	serializer_class = UploadSer

	