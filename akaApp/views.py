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


class ArticleViewset(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

	serializer_class = ArticleSerializer
	queryset = Article.objects.all().order_by('-date')
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	search_fields = ['author__username', 'title', 'text', 'tags__name']
	filter_fields = ('author',)

	def create(self, request):
		s = ArticleSerializer(data=request.data)
		if s.is_valid():
			print(s.validated_data['tags'])
			a = Article.objects.create(
				title=s.validated_data['title'], 
				text=s.validated_data['text'], 
				author=request.user,
				is_blog=s.validated_data['is_blog'],
				is_q=s.validated_data['is_q'],
				is_news = s.validated_data['is_news']
				# tags=s.validated_data['tags']
			)
			# a.tags.set(*s.validated_data['tags'])
			print(s.validated_data['tags'])
			for i in str(s.validated_data['tags'][0]).split(","):
				print(i)
				a.tags.add(i.strip())
			return Response({'status': "created"})
		else:
			return Response(s.errors)


class getArticles(APIView):
	permission_classes = [permissions.AllowAny,]

	def get(self, request, type_art):
		print(type_art)
		if type_art == "blog":
			a = Article.objects.filter(is_blog = True)
		elif type_art == "news":
			a = Article.objects.filter(is_news = True)
		else:
			a = Article.objects.filter(is_q = True)
		s = ArticleSerializer(a, many = True)
		return Response(s.data)



class TagViews(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = TagSerializer(data=request.data)
		if s.is_valid():
			articles = Article.objects.filter(tags__name__in=[s.validated_data['tag']])
			serializer = ArticleSerializer(articles, many=True)
			return Response({"articles": serializer.data})
		else:
			return Response(s.errors)



class FavPostView(APIView):
	permission_classes = [permissions.IsAuthenticated,]

	def post(self, request):
		s = addFavSer(data=request.data)
		if s.is_valid():
			user = User.objects.get(pk = s.validated_data['id'])
			posts = user.fav.all()
			ser = ArticleSerializer(posts, many=True)
			return Response({'posts': ser.data})
		else:
			return Response(s.errors)



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


class CommetViews(viewsets.ModelViewSet):
	permission_classes = [permissions.AllowAny,]
	serializer_class = CommentSerilaizer
	queryset = Comment.objects.root_nodes()
	print(queryset.get_cached_trees())
	filter_backends = [DjangoFilterBackend]
	search_fields = ['article', 'author']
	filter_fields = ('article', 'author')

	def create(self, request):
		s = CommentSerilaizer(data=request.data)
		if s.is_valid():
			parent_commment = None
			parent_commment = s.validated_data.get("parent", None)
			# if Comment.objects.filter(pk=s.validated_data['parent']).exists():
				# parent_commment = Comment.objects.get(pk=s.validated_data['parent'])
			article = None
			# if Article.objects.filter(pk=s.validated_data['article']).exists():
				# article = Article.objects.get(pk=s.validated_data['article'])
			article = s.validated_data['article']
			Comment.objects.create(
				text=s.validated_data['text'], 
				author=request.user,
				parent=parent_commment,
				article=article
			)
			return Response({'status': "created"})
		else:
			return Response(s.errors)