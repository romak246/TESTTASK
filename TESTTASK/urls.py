"""TESTTASK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .swagger import urlpatterns as doc_urls
from TESTTASK.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books', BookAPIView.as_view()),
    path('books/<int:book_id>/', BookOneAPIView.as_view()),
    path('genres/', GenreAPIView.as_view()),
    path('genres/<int:genre_id>/', GenreOneAPIView.as_view()),
    path('currency/', CurrencyAPIView.as_view()),
    path('currency/<int:cur_id>/', CurrencyOneAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserRegisterAPIView.as_view()),

]
urlpatterns += doc_urls