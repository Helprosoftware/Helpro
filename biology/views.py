from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse

def bio(request):
    
    return render(request,"bio.html")

# Create your views here.
