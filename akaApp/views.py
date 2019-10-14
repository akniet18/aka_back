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


class ArticleViewset(viewsets.ModelViewSet):
	permission_classes = [permissions.AllowAny,]
	# authentication_classes = [SessionAuthentication, TokenAuthentication]

	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	filter_backends = [DjangoFilterBackend]
	search_fields = ['id', 'author']
	filter_fields = ('id', 'author')

	def create(self, request):
		# if  request.user.is_authenticated():
			s = ArticleSerializer(data=request.data)
			if s.is_valid():
				Article.objects.create(title=s.validated_data['title'], text=s.validated_data['text'], author=request.user)
				return Response({'status': "created"})
			else:
				return Response(s.errors)
		# else:
			# return Response({'status': "not authentication"})


class addFav(APIView):
	permission_classes = [permissions.IsAuthenticated,]
	authentication_classes = [SessionAuthentication, TokenAuthentication]

	def post(self, request):
		s = addFavSer(data=request.data)
		if s.is_valid():
			a = Article.objects.get(id=s.validated_data['id'])
			if a.favorite.filter(id=request.user.id).exists():
				a.favorite.remove(request.user)
				return Response({"status": "post already exists"})
			else:
				a.favorite.add(request.user)
				return Response({"status": "post add fav"})
