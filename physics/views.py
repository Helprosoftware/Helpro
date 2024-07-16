#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
from django.shortcuts import render
from django.template import loader
from django.template import Template,Context
from django.http import HttpResponse
import math

def physics(request):
    template = loader.get_template('root.html')
    return HttpResponse(template.render())
def vector2(request):
    template = loader.get_template('vectors.html')
    return HttpResponse(template.render())
def vector3(request):
    template = loader.get_template('vectors3.html')
    return HttpResponse(template.render())

def vector4(request):
    template = loader.get_template('vectors4.html')
    return HttpResponse(template.render())
    
def vector2r(request):

    try:
        v1=request.GET["v1"]
        mag1=int(v1)
        ang1=request.GET["ang1"]
        ang1=int(ang1)
        ang1=math.radians(ang1)
        
        v2=request.GET["v2"]
        mag2=int(v2)
        ang2=request.GET["ang2"]
        ang2=int(ang2)
        ang2=math.radians(ang2)
        xmag= mag1*round(math.cos(ang1),2)+mag2*round(math.cos(ang2),2)
        ymag= mag1*round(math.sin(ang1),2)+mag2*round(math.sin(ang2),2)
            #print("xmagnitude:",xmag,"ymagnitude:",ymag)
        totmag=math.sqrt(xmag**2+ymag**2)
        totang= math.degrees(math.atan(ymag/xmag))
        result="angle:",totang,"magnitude",totmag
        previous= "/vectors2"
        
        
        
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        previous = "/vectors2"
        return render(request,"error.html",{"previous":previous})
        
    
#vectors home page
def vector3r(request):
    v1=request.GET["v1"]
    mag1=int(v1)
    ang1=request.GET["ang1"]
    ang1=int(ang1)
    ang1=math.radians(ang1)
    
    v2=request.GET["v2"]
    mag2=int(v2)
    ang2=request.GET["ang2"]
    ang2=int(ang2)
    ang2=math.radians(ang2)

    v3=request.GET["v3"]
    mag3=int(v3)
    ang3=request.GET["ang3"]
    ang3=int(ang3)
    ang3=math.radians(ang3)
    
    xmag= mag1*round(math.cos(ang1),2)+mag2*round(math.cos(ang2),2)+mag3*round(math.cos(ang3),2)
    ymag= mag1*round(math.sin(ang1),2)+mag2*round(math.sin(ang2),2)+mag3*round(math.sin(ang3),2)
        #print("xmagnitude:",xmag,"ymagnitude:",ymag)
    totmag=math.sqrt(xmag**2+ymag**2)
    totang= math.degrees(math.atan(ymag/xmag))
    result="angle:",totang,"magnitude",totmag
    
    previous="/vectors3"
    return render(request,"result.html",{"result":result, "previous":previous})
def vector4r(request):
    v1=request.GET["v1"]
    mag1=int(v1)
    ang1=request.GET["ang1"]
    ang1=int(ang1)
    ang1=math.radians(ang1)
    
    v2=request.GET["v2"]
    mag2=int(v2)
    ang2=request.GET["ang2"]
    ang2=int(ang2)
    ang2=math.radians(ang2)

    v3=request.GET["v3"]
    mag3=int(v3)
    ang3=request.GET["ang3"]
    ang3=int(ang3)
    ang3=math.radians(ang3)

    v4=request.GET["v4"]
    mag4=int(v4)
    ang4=request.GET["ang4"]
    ang4=int(ang4)
    ang4=math.radians(ang4)
    
    xmag= mag1*round(math.cos(ang1),2)+mag2*round(math.cos(ang2),2)+mag3*round(math.cos(ang3),2)+mag4*round(math.cos(ang4),2)
    ymag= mag1*round(math.sin(ang1),2)+mag2*round(math.sin(ang2),2)+mag3*round(math.sin(ang3),2)+mag4*round(math.sin(ang4),2)
        #print("xmagnitude:",xmag,"ymagnitude:",ymag)
    totmag=math.sqrt(xmag**2+ymag**2)
    totang= math.degrees(math.atan(ymag/xmag))
    result="angle:",totang,"magnitude",totmag
    
    previous="/vectors4"
    return render(request,"result.html",{"result":result, "previous":previous})
def vectors(request):
    return render(request,"vectorshome.html",)

def promot(request):
    template = loader.get_template('promot.html')
    return HttpResponse(template.render())
    
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way

