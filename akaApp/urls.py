from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'articles', ArticleViewset, basename='article')

router2 = DefaultRouter()
router2.register(r'comments', CommetViews, basename='comment')


urlpatterns = [
	path('', include(router.urls)),
	path('', include(router2.urls)),
	path('article/add/', addFav.as_view()),
	path('tags/', TagViews.as_view()),

	path('favs/', FavPostView.as_view())
]