from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def gauss(request):
    go=HttpResponse("go")
    return(go)

# Create your views here.
