from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context


def hola(request):
    hola=Httpresponse('hola')
    return(hola)
