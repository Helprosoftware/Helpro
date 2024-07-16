from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def home(request):
    
    template = loader.get_template('hola.html')
    return HttpResponse(template.render())
def info(request):
    template = loader.get_template('info.html')
    return HttpResponse(template.render())
def user(request):
    
    
    try:
        f= open("new_file1.txt", "r")
        f2= open("new_file2.txt", "r")
        f3= open("new_file3.txt", "r")
        f4= open("new_file4.txt", "r")
        f5= open("new_file5.txt", "r")
       
       
        coso1=f
        coso2=f2
        coso3=f3
        coso4=f4
        coso5=f5
    except:
        nada="nada"
        coso1=nada
        coso2=nada
        coso3=nada
        coso4=nada
        coso5=nada
        
        
   
    
    doc = open("C:/Users/hp/Desktop/hprweb/home/templates/user.html")
    read=Template(doc.read())
    doc.close()
    ctx= Context({"coso1":coso1,"coso2":coso2,"coso3":coso3,"coso4":coso4})
    documento=read.render(ctx)
    return HttpResponse(documento)



def addgauss(request):
    place=int(request.GET["place"])
    f = open('new_file.txt', 'r')    
    lines = f.readlines()
    lines[place] = "new\n"    
    f.close()  

    f = open('new_file.txt', 'w')
    f.writelines(lines)
    f.close()
    
   
    name="name"
    previous="/maths"
    doc = open("C:/Users/hp/Desktop/hprweb/members/templates/add.html")
    read=Template(doc.read())
    doc.close()
    ctx= Context({"name":name, "previous":previous})
    documento=read.render(ctx)
    return HttpResponse(documento)
    
    
# Create your views here.
