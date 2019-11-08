from django.urls import path, include
from .views import *

urlpatterns = [
	path('register/', Register.as_view()),
	path('login/', Login.as_view()),
	path('<int:pk>/', getUser.as_view()),
]