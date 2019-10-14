from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'articles', ArticleViewset, basename='user')

urlpatterns = [
	path('', include(router.urls)),
	path('article/add/', addFav.as_view())
]