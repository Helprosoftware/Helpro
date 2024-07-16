from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('physics/', views.physics, name='physics'),
    #vectors...
    #path('vectors', views.vectors, name='vectors'),
    path('vectors2/', views.vector2, name="vectors2"),
    path('vectsult2/',views.vector2r, name="vectsult2"),
    path('vectors3/', views.vector3, name="vectors3"),
    path('vectsult3/',views.vector3r,name="vectsult3"),
    path('vectors4/', views.vector4, name="vectors4"),
    path('vectsult4/',views.vector4r,name="vectsult4"),
    path('promot/', views.promot, name="promot"),
    
    

]
