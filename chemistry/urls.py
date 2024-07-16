from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('chemistry', views.chem, name='members'),
    #path('mr/',views.Mr, name='Mr'),
    path('mr2/',views.mr2, name='mr2'),
    path('mr3/',views.mr3, name='mr3'),
    path('mr4/',views.mr4, name='mr4'),
    path('mrsult2/', views.promr2, name='marsult2'),
    path('mrsult3/', views.promr3, name='marsult3'),
    path('mrsult4/', views.promr4, name='marsult4'),
    
    path('molec2/', views.molec2, name='molec2'),
    path('molec3/', views.molec3, name='molec3'),
    path('molec4/', views.molec4, name='molec4'),
    
    path('molec2tvm/', views.molec2tvm, name='molec2tvm'),
    path('molec3tvm/', views.molec3tvm, name='molec3tvm'),
    path('molec4tvm/', views.molec4tvm, name='molec4tvm'),
    
    path('molecsult2/', views.molecsult2, name='molec2'),
    path('molecsult3/', views.molecsult3, name='molec3'),
    path('molecsult4/', views.molecsult4, name='molec3'),
    
    path('molecsult2tvm/', views.molecsult2tvm, name='molecsult2tvm'),
    path('molecsult3tvm/', views.molecsult3tvm, name='molecsult3tvm'),
    path('molecsult4tvm/', views.molecsult4tvm, name='molecsult4tvm'),
    #path('question/', views.question, name = 'question2')
]
    
