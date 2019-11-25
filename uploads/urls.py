from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'', UploadsView, basename='uploads')

# router2 = DefaultRouter()
# router2.register(r'comments', CommetViews, basename='comment')


urlpatterns = [
	path('', include(router.urls))
]