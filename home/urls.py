from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/' , views.home, name='home'),
    path('info/', views.info, name='info'),
    path('users/', views.user, name='user'),
    path('gaussadd/', views.addgauss, name='addgauss'),
]

