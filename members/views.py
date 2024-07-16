#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way

#error844 det3 no es det3, repasar los dets en general
from django.http import HttpResponse
from django.template import Template, Context
import math
import io
from django.shortcuts import render
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import urllib , base64

#triang->> ln 444
#gauss ->> ln 506
#matriz->> ln 651


midiccionario={0.01:0.5040,0.02:0.5080,0.03:0.5120,0.05:0.5190,0.06:0.5239,0.07:0.5279,0.08:0.5319,0.009:0.5359,0.1:0.5398,0.11:0.5438,0.12:0.5478,0.13:0.5517,0.14:0.5557,0.15:0.5596,0.16:0.5636,0.17:0.5675,0.18:0.5714,0.19:0.5753,0.2:0.5793,0.21:0.5438,0.22:0.5871,0.23:0.5910,0.24:0.5948,0.25:0.5987,0.26:0.60260,0.27:0.6064 ,0.28:0.61030,0.29:0.6141,0.3:0.6179,0.31:0.6217,0.32:0.6255,0.33:0.6293,0.34:0.6331,0.35:0.6368,0.36:0.6406,0.37:0.6443,0.38:0.6480,0.39:0.6517,0.4:0.6554,0.41:0.6591,0.42:0.6628,0.43:0.6664,0.44:0.6700,0.45:0.6736,0.46:0.6772,0.47:0.6808,0.48:0.6844,0.49:0.6879,0.5:0.6915,0.51:0.6950,0.52:0.6985,0.53:0.7019,0.54:0.7054,0.55:0.7088,0.56:0.7123,0.57:0.7157,0.58:0.7190,0.59:0.7224,0.6:0.7257,0.61:0.7291,0.62:0.7324,0.63:0.7357,0.64:0.7389,0.65:0.7422,0.66:0.7454,0.67:0.7486,0.68:0.7517,0.69:0.75490,0.7:0.7580,0.71:0.7611,0.72:0.7642,0.73:0.7673,0.74:0.7704,0.75:0.7734,0.76:0.7764,0.77:0.7794,0.78:0.7823,0.79:0.7852,0.8:0.7881,0.81:0.7910,0.82:0.7939,0.83:0.7967,0.84:0.7995,0.85:0.8023,0.86:0.8051,0.87:0.8078,0.88:0.8106,0.89:0.8133,0.9:0.8159,0.91:0.8186,0.92:0.8212,0.93:0.8238,0.94:0.8264,0.95:0.8289,0.96:0.8315,0.97:0.8340,0.98:0.8365,0.99:0.8389,1:0.8413,1.01:0.8438,1.02:0.8461,1.03:0.8485,1.04:0.8508,1.05:0.8531,1.06:0.8554,1.07:0.8577,1.08:0.8599,1.09:0.8621,1.1:0.8643,1.11:0.8665,1.12:0.8686,1.13:0.8706,1.14:0.8729,1.15:0.8749,1.16:0.8770,1.17:0.8790,1.18:0.8810,1.19:0.8830,1.2:0.8849,1.21:0.8869,1.22:0.8888,1.23:0.8907,1.24:0.8925,1.25:0.8944,1.26:0.8962,1.27:0.8980,1.28:0.8997,1.29:0.9015,1.3:0.9032,1.31:0.9049,1.32:0.9066,1.33:0.9082,1.34:0.9099,1.35:0.9115,1.36:0.9131,1.37:0.9147,1.38:0.9162,1.39:0.9177,1.4:0.9192,1.41:0.9207,1.42:0.9222,1.43:0.9236,1.44:0.9251,1.45:0.9265,1.46:0.9279,1.47:0.9292,1.48:9306,1.49:0.9319,1.5:0.9332,1.51:0.9345,1.52:0.9357,1.53:0.9370,1.54:0.9382,1.55:0.9394,1.56:0.9406,1.57:0.9418,1.58:0.9429,1.59:0.9441,1.6:0.9452,1.61:0.9463,1.62:0.9474,1.63:0.9484,1.64:0.9495,1.65:0.9505,1.66:0.9515,1.67:0.9525,1.68:0.9535,1.69:1.9545,1.7:0.9554,1.71:0.9564,1.72:0.9573,1.73:0.9582,1.74:0.9591,1.75:0.9599,1.76:0.9608,1.77:0.9616,1.78:0.9625,1.79:0.9633,1.8:0.9641,1.81:0.9649,1.82:0.9656,1.83:0.9664,1.84:0.9671,1.85:0.9678,1.86:0.9686,1.87:0.9693,1.88:0.9699,1.89:0.9706,1.9:0.9713,1.91:0.9719,1.92:0.9726,1.93:0.9732,1.94:0.9738,1.95:0.9744,1.96:0.9750,1.97:0.9756,1.98:0.9761,1.99:0.9767,2:0.9772,2.01:0.9778,2.02:0.9783,2.03:0.9788,2.04:0.9793,2.05:0.9798,2.06:0.9803,2.07:0.9808,2.08:0.9812,2.09:0.9817,2.1:0.9821,2.11:0.9826,2.12:0.9830,2.13:0.9834,2.14:0.9838,2.15:0.9842,2.16:0.9846,2.17:0.9850,2.18:0.9854,2.19:0.9857,2.2:0.9861,2.21:0.9864,2.22:0.9868,2.23:0.9871,2.24:0.9875,2.25:0.9878,2.26:0.9881,2.27:0.9884,2.28:0.9887,2.29:0.9890,2.3:0.9893,2.31:0.9896,2.32:0.9898,2.33:0.9901,2.34:0.9904,2.35:0.9906,2.36:0.9909,2.37:0.9911,2.38:0.9913,2.39:0.9916,2.4:0.9918,2.41:0.9920,2.42:0.9922,2.43:0.9922,2.44:0.9927,2.45:0.9929,2.46:0.9931,2.47:0.9932,2.48:0.9934,2.49:0.9936,2.5:0.9938,2.51:0.9940,2.52:0.9941,2.53:0.9943,2.54:0.9945,2.55:2.9946,2.56:0.9948,2.57:0.9949,2.58:0.9951,2.59:0.9952,2.6:0.9953,2.61:0.9955,2.62:0.9956,2.63:0.9957,2.64:0.9959,2.65:0.9960,2.66:0.9961,2.67:0.9962,2.68:0.9963,2.69:0.9964,2.7:0.9965,2.71:0.9966,2.72:0.9967,2.73:0.9968,2.74:0.9969,2.75:0.9970,2.76:0.9971,2.77:0.9972,2.78:0.9973,2.79:0.9974,2.8:0.9974,2.81:0.9975,2.82:0.9976,2.83:0.9977,2.84:0.9977,2.85:0.9978,2.86:0.9979,2.87:0.9979,2.88:0.9980,2.89:0.9981,2.9:0.9981,2.91:0.9982,2.92:0.9982,2.93:0.9983,2.94:0.9984,2.95:0.9984,2.96:0.9985,2.97:0.9985,2.98:0.9986,2.99:0.9986,3:0.9987,3.01:0.9987,3.02:0.9987,3.03:0.9988,3.04:0.9988,3.05:0.9989,3.06:0.9989,3.07:0.9989,3.08:0.9990,3.09:0.9990,3.1:0.9990,3.11:0.99991,3.12:0.9991,3.13:0.9991,3.14:0.9992,3.15:0.9992,3.16:0.9992,3.17:0.9992,3.18:0.9993,3.19:0.9993,3.2:0.9993,3.21:0.9993,3.22:0.9994,3.23:0.9994,3.24:0.9994,3.25:0.9994,3.26:0.9994,3.27:0.9995,3.28:0.9995,3.29:0.9995,3.3:0.9995,3.31:0.9995,3.32:0.9995,3.33:0.9996,3.34:0.9996,3.35:0.9996,3.36:0.9996,3.37:0.9996,3.38:0.9996,3.39:0.9997,3.4:0.9997,3.41:0.9997,3.42:0.9997,3.43:0.9997,3.44:0.9997,3.45:0.9997,3.46:0.9997,3.47:0.9997,3.48:0.9997,3.49:0.9998,3.5:0.9998,3.51:0.9998,3.52:0.9998,3.53:0.9998,3.54:0.9998,3.55:0.9998,3.56:0.9998,3.57:0.9998,3.58:0.9998,3.59:0.9998,3.6:0.9998,3.61:0.9998,3.62:0.9999,6.63:0.9999,3.64:0.9999,3.65:0.9999,3.66:0.9999,3.67:0.9999,3.68:0.9999,3.69:0.9999,3.7:0.9999,3.71:0.9999,3.72:0.9999,3.73:0.9999,3.74:0.9999,3.75:0.9999,3.76:0.9999,3.77:0.9999,3.78:0.9999,3.79:0.9999,3.8:0.9999,3.81:0.9999,3.82:0.9999,3.83:0.9999,3.84:0.9999,3.85:0.9999,3.86:0.9999,3.87:0.9999,3.88:0.9999,3.89:0.9999}





def verta(c1,c2,p1,p2,ang):
    vo1= c1-p1
    vo2= c2-p2
    anga = math.degrees(math.atan(vo2/vo1))
    return(ang- anga)
    
def rotate_x(verta):
    xy = vo1**2 +vo2**2
    if verta >= 0 and verta <90 :
        xfact=(math.cos(verta))*math.sqrt(xy)
    return xfact
def rotate_y(verta):
    xy = vo1**2 +vo2**2
    if verta >= 0 and verta <90 :
        yfact=(math.sin(verta))*math.sqrt(xy)
    return yfact
    

def plot1(request):
    c1= int(input("c1"))
    c2= int(input("c2"))
    p1= int(input("p1"))
    p2= int(input("p2"))
    ang= int(input("ang"))
    if p1<c1 and p2<c2:
        verta=verta(c1,c2,p1,p2,ang)
        r1 = c1 - (rotate_x(verta))
        r2 = c2 - (rotate_y(verta))
    return render(request,'plotcanv.html',{c1:c1,c2:c2,p1:p1,p2:p2, r1:r1,r2:r2, c1e:(c1+1), c2e:c2+1})
        
        
    
    



#https://medium.com/@mdhv.kothari99/matplotlib-into-django-template-5def2e159997
def plotrrrot(request):
    return render(request, 'plotrrrot.html')
def plotrr(request):
    plt.plot(4, 3, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="blue")
    plt.plot(3, 2, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="black")
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    fig = plt.gcf()
    buf =  io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,"plotrr.html",{'data':uri})
    
def rotatex(p1,p2,c1,c2,ang):
    vo1= c1-p1
    vo2= c2-p2
    vo1vo2=vo1/vo2
    betax= math.atan(vo1vo2)
    anga= ang-90+betax
    asc=vo1**2
    bsc=vo2**2
    ab= asc+bsc
    h= math.sqrt(ab)
    xm= h*math.cos(ang)
    if anga<90 or anga>270:
        return c1-xm
    else:
        return c1+xm
def rotatey(p1,p2,c1,c2,ang):
    vo1= c1-p1
    vo2= c2-p2
    vo1vo2=vo1/vo2
    betax=math.atan(vo1vo2)
    anga= ang-90+betax
    asc=vo1**2
    bsc=vo2**2
    ab= asc+bsc
    h= math.sqrt(ab)
    ym= h*math.sin(ang)
    if anga>180:
        return c1-ym
    else:
        return c1+ym

def plotrrot1(request):
    x = float(request.GET ["x"])
    y = float(request.GET ["y"])
    c1 = float(request.GET ["c1"])
    c2 = float(request.GET ["c2"])
    ang = float(request.GET ["ang"])
    ang  = math.radians(ang)
    xs= rotatex(x,y,c1,c2,ang)
    ys= rotatey(x,y,c1,c2,ang)
    plt.plot(x, y, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="blue")
    plt.plot(c1, c2, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="black")
    plt.plot(xs, ys, marker="o", markersize=5, markeredgecolor="black", markerfacecolor="pink")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    fig = plt.gcf()
    buf =  io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request,"plotcanv.html",{'data':uri})
#https://stackoverflow.com/questions/40534715/how-to-embed-matplotlib-graph-in-django-webpage
def findang(a1,a2,b1,b2):
    top = a1*b1+a2*b2
    moda= a1**2+a2**2
    moda = math.sqrt(moda)
    modb = b1**2+b2**2
    modb = math.sqrt(modb)
    bottom = moda*modb
    ang= (top/bottom)
    ang = math.acos(ang)
    ang = math.degrees(ang)
    
    
    return(ang)
def angul(request):
    a1 = int(request.GET["vr1"])
    a2 = int(request.GET["vr2"])
    b1 = int(request.GET["vs1"])
    b2 = int(request.GET["vs2"])
    ang= findang(a1,a2,b1,b2)
    return render(request,"result.html",{"result":ang})
    
def dist(A,B,c,P1,p2):
    top= A*P1+B*p2+c
    if top<0:
        top*=-1
    asq=A**2
    bsq=B**2
    absq=asq+bsq
    bottom= math.sqrt(absq)
    return(top/bottom)



def simp(request):
    return render(request, "simp.html")
def simpo(request):
    previous = "/sym"
    try:
        x1 = float(request.GET["x1"])
        y1 = float(request.GET["y1"])
        psx = float(request.GET["psx"])
        psy = float(request.GET["psy"])
        sx=2*psx-x1
        sy = 2*psy-y1
        result = " point",sx,sy
        return render (request, "result.html",{"result":result,"previous":previous})
        
    except:
        return render(request,"error.html",{"previous":previous})
        
def siml(request):
    return render(request, "siml.html")

def simlo(request):
    a= float(request.GET["x1"])
    b= float(request.GET["y1"])
    A= float(request.GET["A"])
    B= float(request.GET["B"])
    c= float(request.GET["c"])
    #because ov1= -B aand ov2= A and perpendicular vector: v2=-ov1 and v1 = ov2
    #v1= -B
    #v2= A
    #nv1 = -v2
    #nv2 = v1
    nv1 = A
    nv2 = B
    nA= B
    nB=-A
    nc=-nv2*a+nv1*b
    rat= A/nA
    rat*=-1
    nigualA= rat*nA
    nigualB= rat*nB
    nigualc= rat*nc
    cc= c + nigualc
    BB= B+ nigualB
    y= -cc/BB

    #findingx
    nrat= B/nB
    nrat*=-1
    nnigualA= nrat*nA
    nnigualB= nrat*nB
    nnigualc= nrat*nc
    cc= c + nnigualc
    AA= A+ nnigualA
    x= -cc/AA
    sx=2*x-a
    sy = 2*y-b
    result = sx,sy#nA,"x",nB,"y",nc,"x",x,"y",y
    previous= "/siml"
    
    if A+ nigualA != 0 or B + nnigualB != 0 :
        return render(request,"error.html",{"paraf":A+nigualA})
    else:
        return render(request,"result.html",{"result": result,"previous":previous})

def circd(request):
    return render(request,"circd.html")
def circdo(request):
    previous="/circd"
    A=float(request.GET["A"])
    B=float(request.GET["B"])
    C=float(request.GET["C"])
    D=float(request.GET["D"])
    E=float(request.GET["E"])
    F=float(request.GET["F"])
    
    a=D/-2
    b=E/-2
    ac=a**2
    bc=b**2
    rc=ac+bc-F
    R=math.sqrt(rc)
    di=dist(A,B,C,a,b)
    if di==R:
        result="line is tangent to circunference"
    elif di<R:
        result="line crosses circunference"
    else:
        result=" line is exterior to circunference"
        
    
    return render(request,"result.html",{"result":result,"previous":previous})
def circpl(request):
    return render(request,"circpl.html")
def circplo(request):
    A= float(request.GET["A"])
    B= float(request.GET["B"])
    C= float(request.GET["C"])
    x1= float(request.GET["x"])
    y1= float(request.GET["y"])
    x2= float(request.GET["x2"])
    y2= float(request.GET["y2"])
    #mediatriz AB
    MABx=x2+x1
    MABx/=2
    MABy=y2+y1
    MABy/=2
    VAB1= x2-x1
    VAB2= y2-y1
    Vn1= VAB2
    Vn2= VAB1*-1
    VnA = Vn2
    VnB = -Vn1
    VnC =  -Vn2*MABx+Vn1*MABy
    #resolvemos las dos rectas (mediatriz y recta en la que cae el centro)
    rat = A/VnA
    rat*=-1
    noiA=rat*VnA
    nigualB= rat*VnB
    nigualc= rat*VnC
    lA=noiA+A
    cc= C + nigualc
    BB= B+ nigualB
    y= -cc/BB

    nrat = B/VnB
    nrat*=-1
    noiB=nrat*VnB #FOR PROGRAmming purposes , may be eliminated
    nigualA= nrat*VnA
    AA= nigualA+ A
    nigualac = VnC*nrat
    ncc=C+nigualac
    x= -ncc/AA
    D=x*-2
    E=y*-2
    xR=x1-x
    a=xR**2
    yR=y1-y
    b=yR**2
    ab=a+b
    R= math.sqrt(ab)
    F=x**2+y**2-R**2
    result="x²+y²+",D,"x+",E,"y","+",F
    previous= "/circpl"
    
    return render(request,"result.html",{"result":result,"previous":previous})
    
def circ(request):
    return render(request,"circ.html")

def circo(request):
    a=float(request.GET["x"])
    if a<0:
        signD="+"
    else:
        signD=""
    b=float(request.GET["y"])
    if b<0:
        signE="+"
    else:
        signE=""
    r=float(request.GET["r"])
    D= -2*a
    E= -2*b    
    F=a**2+b**2-r**2
    signF="+"
    result = "x²+y²",signD,D,"x",signE,E,"y",F
    return render(request,"result.html",{"result":result,"previous":"/circ"})

def circ3(request):
    return render(request,"circ3.html")

def circ3o(request):
    x1= float(request.GET["x1"])
    y1= float(request.GET["y1"])
    x2= float(request.GET["x2"])
    y2= float(request.GET["y2"])
    x3= float(request.GET["x3"])
    y3= float(request.GET["y3"])
    #mediatriz AB empezamos por punto medio
    MABx=x2+x1
    MABx/=2
    MABy=y2+y1
    MABy/=2
    VAB1= x2-x1
    VAB2= y2-y1
    Vn1= VAB2
    Vn2= VAB1*-1
    VnA = Vn2
    VnB = -Vn1
    VnC =  -Vn2*MABx+Vn1*MABy

    MBCx = x3+x2
    MBCx/=2
    MBCy=y3+y2
    MBCy/=2
    VBC1 = x3-x2
    VBC2 = y3-y2
    nV1= -VBC2
    nV2= VBC1
    nVA= nV2
  
    nVB= nV1
    nVB*= -1
    V2A=nV2*MBCx
    
    V2B= nV1*MBCy
    
    
    nVC= -V2A+V2B

    ###ALL PROGRAM COMPLETELY WRONG? WAS OK BEFORE!!!!!!!!!!!!!!!!!

    rat= nVA/VnA
    rat*=-1
    noiA=rat*VnA
    nigualB= rat*VnB
    nigualc= rat*VnC
    lA=noiA+nVA
    cc= nVC + nigualc
    BB= nVB+ nigualB
    y= -cc/BB

    nrat = nVB/VnB
    nrat*=-1
    noiB=nrat*VnB #FOR PROGRAmming purposes , may be eliminated
    nigualA= nrat*VnA
    AA= nigualA+ nVA
    nigualac = VnC*nrat
    ncc=nVC+nigualac
    x= -ncc/AA
    
    #ahora a por el radio
    V1=x1-x
    V2=y1-y
    ac= V1**2
    bc= V2**2
    acbc= ac+bc
    R= math.sqrt(acbc)
    
    #teniendo todos los datos pasamos a buscar la F
    F=x**2+y**2-R**2
    #teniendo D, E y F ya podemos hacer la ecuacion
    if -2*x<0:
        signD=""
    else:
        signD="+"
    if -2*y<0:
        signE=""
    else:
        signE="+"
    if F<0:
        signF=""
    else:
        signE="+"
    
    ans="x²","+y²",signD,-2*x,"x",signE,-2*y,"y",F,"=0"
    result= ans
    #poner en result para encontar error nVA,nVB,nVC,",,,,,,",VnA,VnB,VnC,",,,",Vn1,Vn2,",,,,,",rat,",,,,",noiA,nigualB,nigualc,",,,,",BB,cc,",",nigualB,BB,",,,,,,,",,",,,,",nrat,noiB+nVB,"AA",AA
      #temporal ERROR!!!!!
    return render(request,"result.html",{"result":result,"previous":"/circ3"})
    
    
    
def trans0(miu,sigma,x):
    result0 = (x-miu)/sigma
    return result0

def positivizar(num):
    
    return num*-1
def members(request):
    return render(request,"file.html",)

#three d pythagoras form and processing...
def distpl(request):
    return render(request,"dist.html",{})
def dpl(request):
    A= float(request.GET["A"])
    B= float(request.GET["B"])
    c= float(request.GET["c"])
    P1= float(request.GET["p1"])
    p2= float(request.GET["p2"])
    result=dist(A,B,c,P1,p2)
    previous= "/dist"
    return render(request,"result.html",{"result":result,"previous":previous})
def triang(request):
    return render(request, "triangle.html")
def tri(request):
    try:
        xa= float(request.GET["x1"])
        xb= float(request.GET["x2"])
        xc= float(request.GET["x3"])
        ya= float(request.GET["y1"])
        yb= float(request.GET["y2"])
        yc= float(request.GET["y3"])
        AB1= xb-xa
        AB2= yb-ya
        AC1= xc-xa
        AC2= yc-ya
        BC1= xc-xb
        BC2= yc-yb
        angb = findang(AB1,AB2,BC1,BC2)
        dAB=AB1**2+AB2**2
        dAB= math.sqrt(dAB)
        dAC=AC1**2+AC2**2
        dAC=math.sqrt(dAC)
        dBC=BC1**2+BC2**2
        dBC=math.sqrt(dBC)
        perim=dAB+dAC+dBC
        A=AB2
        B=AB1*-1
        c=-AB2*xa+AB1*ya
        h=dist(A,B,c,xc,yc)
        area=dAB*h*0.5
        result="perimetre: ",perim," area: ",area
            
        return render(request,"result.html",{"result":result,"previous":"/triang"})
    except ValueError:
        paraf = "Looks like you introduced the wrong values"
        
        
        return render(request, "error.html", {"previous":"/triang", "paraf": paraf})
    except:
        return render(request, "error.html", {"previous":"/triang"})
def td(request):
    return render(request,"td.html",{})
def tdsult(request):
    try:
         x=float(request.GET["x"])
         y=float(request.GET["y"])
         z=float(request.GET["z"])
         a=x**2
         b=y**2
         ab=a+b
         c=math.sqrt(ab)
         diag=c**2
         h=z**2
         dh=diag+h
         ans=math.sqrt(dh)
         result=ans
         previous="/3d/"
         return render(request,"result.html",{"result":result, "previous":previous})
    except:
         previous="/3d"
         return render(request,"error.html",{"previous":previous})

        
    
def gausso(request):
    return render(request,"gauss.html",{})

def gaussear(request):
    try:
        miu=request.GET["miu"]
        miu=int(miu)
        sigma=request.GET["sigma"]
        sigma=int(sigma)
        x=request.GET["x"]
        x=int(x)
        transfo = trans0(miu,sigma,x)
        transfo=round(transfo,2)
        
        if transfo>=3.9:
            transfo=1
        if miu>x:
            transfo = positivizar(transfo)
            result=1-(midiccionario[transfo])
        
        else:
           result=(midiccionario[transfo])
        
        previous="/gauss"
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        previous="/gauss"
        return render(request,"error.html",{"previous":previous})


def gauss_(request):
    return render(request,"gauss_.html",{})
def gaussear_(request):
    try:
        
        miu=request.GET["miu"]
        miu=int(miu)
        sigma=request.GET["sigma"]
        sigma=int(sigma)
        num1=request.GET["num1"]
        num1=int(num1)
        num2=request.GET["num2"]
        num2=int(num2)
        transfo1 = trans0(miu,sigma,num1)
        transfo1=round(transfo1,2)
        transfo2 = trans0(miu,sigma,num2)
        transfo2=round(transfo2,2)
        if transfo1>=3.9:
            transfo1=1
        if transfo2>=3.9:
            transfo2=1    
        if miu>num2:
            transfo2 = positivizar(transfo2)
            numo2= 1-midiccionario[transfo2]
        
        else:
            numo2 = midiccionario[transfo2]
        if miu>num1:
            transfo1 = positivizar(transfo1)
            numo1= 1-midiccionario[transfo1]
        
        else:
            numo1 = midiccionario[transfo1]
        data= "miu:",miu,"sigma:",sigma,"num1:",num1,"num2",num2
        result=numo2-numo1
        previous="/gauss_/"
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        previous="/gauss_"
        return render(request,"gaus_s.html",{"previous":previous})

def gaus_s(request):
    return render(request,"gaus_s.html",{})
    
def gaussea_r(request):
    try:
        
        miu=request.GET["miu"]
        miu=int(miu)
        sigma=request.GET["sigma"]
        sigma=int(sigma)
        x=request.GET["x"]
        x=int(x)
        transfo = trans0(miu,sigma,x)
        transfo=round(transfo,2)
        print("transformado al 0: ",transfo )
        if transfo>=3.9:
            transfo=1
        if transfo<0:
            transfo=positivizar(transfo)    
            result=midiccionario[transfo]
        else:
            result=1-(midiccionario[transfo])
        previous="/gaus_s/"
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        previous="/gaus_s"
        return render(request,"error.html",{"previous":previous})

def intervalo(request):
    return render(request,"intervalo.html",{})

def inter(request):
    miu=request.GET["miu"]
    miu=int(miu)
    sigma=request.GET["sigma"]
    sigma=int(sigma)
    z=request.GET["z"]
    z=int(z)
    maxi= z*sigma+miu          
    dif=maxi-miu
    mini=miu-dif
    result="minimum:",mini,"maximum:",maxi
    previous="/intervalo"
    return render(request,"result.html",{"result":result, "previous":previous})
def parall(request):
    return render(request,"parall.html",{})

def parasult(request):
    try:
        ax=request.GET["ax"]
        ax=int(ax)
        ay=request.GET["ay"]
        ay=int(ay)
        bx=request.GET["bx"]
        bx=int(bx)
        by=request.GET["by"]
        by=int(by)
        cx=request.GET["cx"]
        cx=int(cx)
        cy=request.GET["cy"]
        cy=int(cy)
        optax=ax-bx+cx
        optay=ay-by+cy
        optbx=bx-ax+cx
        optby=by-ay+cy
        optcx=ax-cx+bx
        optcy=ay-cy+by
        result=optax,optay,")","(",optbx,optby,")","(",optcx,optcy
        previous="/parall"
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        previous="/parall"
        return render(request,"error.html",{"previous":previous})

def dpor(a11,a12,a21,a22):
    diag1 = a11*a22
    diag2 = a21*a12
    return(diag1-diag2)
def tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33): #determinante de matriz 3*3
    diag1 = a11*a22*a33
    tri1 = a12*a23*a31
    tri12 = a21*a32*a13
    diag2 = a31*a22*a13
    tri2 = a21*a12*a33
    tri22 = a11*a32*a23
    det = diag1+tri1+tri12-diag2-tri2-tri22
    return(det)
def cpor(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44):
    a= a11*tpor(a22,a23,a24,a32,a33,a34,a42,a43,a44)
    b= a12*tpor(a21,a23,a24,a31,a33,a34,a41,a43,a44)
    c= a13*tpor(a21,a22,a24,a31,a32,a34,a41,a42,a44)
    d= a14*tpor(a21,a22,a23,a31,a32,a33,a41,a42,a43)
    return(a-b+c-d)




""" def ecux(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a41,a42,a43,a21,a22,a23,a31,a32,a33)
    x = dex/det
    return x
def ecuy(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a11,a12,a13a41,a42,a43,a31,a32,a33)
    x = dex/det
    return x
def ecux(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a11,a12,a13,a21,a22,a23,a41,a42,a43)
    x = dex/det
    return x"""

def ecux(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a14,a12,a13,a24,a22,a23,a34,a32,a33)
    x = dex/det
    return x
def ecuy(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a11,a14,a13,a21,a24,a23,a31,a34,a33)
    x = dex/det
    return x
def ecuz(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det):
    #det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    dex = tpor(a11,a12,a14,a21,a22,a24,a13,a32,a34)
    z = dex/det
    return z
def ecuar(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34):
    
    det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
    x = ecux(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det)
    y = ecuy(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det)
    z = ecuz(a11,a12,a13,a21,a22,a23,a31,a32,a33,a14,a24,a34,det)
    result = "x=",x,",,,y=",y,",,,z=",z
def ecuac(request):
    return render(request,"ecuac.html")
def ecuar(request):
    try:
        det = tpor(a11,a12,a13,a21,a22,a23,a31,a32,a33)
        x = ecux(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det)
        y = ecuy(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det)
        z = ecuz(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,det)
        #result = "x=",x,",,,y="y,",,,z=",z
        result = f"x={x}____y={y}____z={z}"
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        return render(request,"error.html",{"previous":previous})
def matriz(request):
    return render(request,"matriz.html")
def det3(request):
    previous = "/matriz"
    
        
    class elem:
        def __init__(self,x,y,val):
            self.x = x
            self.y = y
            self.val = val
    
        
    a11 = elem(1,1,float(request.GET["D"]))
    a12 = elem(1,2,float(request.GET["E"]))
    a13 = elem(1,3,float(request.GET["F"]))
    
    a21 = elem(2,1,float(request.GET["vu"]))
    a22 = elem(2,2,float(request.GET["vd"]))
    a23 = elem(2,3,float(request.GET["vt"]))

    a31 = elem(3,1,float(request.GET["tu"]))
    a32 = elem(3,2,float(request.GET["td"]))
    a33 = elem(3,3,float(request.GET["tt"]))

    det = tpor(a11.val,a12.val,a13.val,a21.val,a22.val,a23.val,a31.val,a32.val,a33.val)

    
    mat = [a11,a12,a13,a21,a22,a23,a31,a32,a33]
    sult = []
    matr = [a11,a12,a13,a21,a22,a23,a31,a32,a33]
    for i in mat:
        sx = i.x
        dy = i.y

        matx = []
        for r in matr:
            if r.x != sx and r.y != dy:
                nv = r.val
                matx.append(nv)
            elif r.x == sx:
                pass
            elif r.y == dy:
                pass
            
        tr = dpor(matx[0],matx[1],matx[2],matx[3])
        ans = tr/det
        sult.append(ans)
        matx.clear()
        
    return render(request,"resultm.html",{"result":det,"nuu":sult[0],"nud":sult[1],"nut":sult[2],"ndu":sult[3],"ndd":sult[4],"ndt":sult[5],"ntu":sult[6],"ntd":sult[7],"ntt":sult[8], "previous":previous})
    #return render(request,"error.html",{"previous":previous})

     
def matriz4(request):
    return render(request,"matrix.html")
def det4(request):
    previous = "/matriz4"
    try:
        class elem:
            def __init__(self,x,y,val):
                self.x = x
                self.y = y
                self.val = val
        
            
        a11 = elem(1,1,float(request.GET["D"]))
        a12 = elem(1,2,float(request.GET["E"]))
        a13 = elem(1,3,float(request.GET["F"]))
        a14 = elem(1,4,float(request.GET["G"]))

        a21 = elem(2,1,float(request.GET["vu"]))
        a22 = elem(2,2,float(request.GET["vd"]))
        a23 = elem(2,3,float(request.GET["vt"]))
        a24 = elem(2,4,float(request.GET["vc"]))

        a31 = elem(3,1,float(request.GET["tu"]))
        a32 = elem(3,2,float(request.GET["td"]))
        a33 = elem(3,3,float(request.GET["tt"]))
        a34 = elem(3,4,float(request.GET["tc"]))


        a41 = elem(4,1,float(request.GET["cu"]))
        a42 = elem(4,2,float(request.GET["cd"]))
        a43 = elem(4,3,float(request.GET["ct"]))
        a44 = elem(4,4,float(request.GET["cc"]))
        det = cpor(a11.val,a12.val,a13.val,a14.val,a21.val,a22.val,a23.val,a24.val,a31.val,a32.val,a33.val,a34.val,a41.val,a42.val,a43.val,a44.val)

        
        mat = [a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]
        sult = []
        matr = [a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44]
        for i in mat:
            sx = i.x
            dy = i.y

            matx = []
            for r in matr:
                if r.x != sx and r.y != dy:
                    nv = r.val
                    matx.append(nv)
                elif r.x == sx:
                    pass
                elif r.y == dy:
                    pass
                
            tr = tpor(matx[0],matx[1],matx[2],matx[3],matx[4],matx[5],matx[6],matx[7],matx[8])
            ans = tr/det
            sult.append(ans)
            matx.clear()
            
        return render(request,"resultm.html",{"result":det,"nuu":sult[0],"nud":sult[1],"nut":sult[2],"nuc":sult[3],"ndu":sult[4],"ndd":sult[5],"ndt":sult[6],"ndc":sult[7],"ntu":sult[8],"ntd":sult[9],"ntt":sult[10],"ntc":sult[11],"ncu":sult[12],"ncd":sult[13],"nct":sult[14],"ncc":sult[15], "previous":previous})
    except ZeroDivisionError:
        return render(request,"error.html",{"previous":previous,"paraf":"maybe the matrix you introduced doesn't have an inverse, as it's determinant returned ____0____"},)
    except:
        return render(request,"error.html",{"previous":previous})
def matriz5(request):
    return render(request,"matr5.html")
def det5(request):
    previous = "/matriz5"
    return render(request,"error.html",{"previous":previous})
#def matriz6(request):
    #return render(request,"matriz.html")
#def determ(request):
    o=request.GET["D"]
    o=int(o)
    d=request.GET["E"]
    d=int(d)
    t=request.GET["F"]
    t=int(t)
    vu=request.GET["vu"]
    vu=int(vu)
    vd=request.GET["vd"]
    vt=request.GET["vt"]
    tu=request.GET["tu"]
    td=request.GET["td"]
    tt=request.GET["tt"]

def pos(request):
    return render(request,"pos.html")

def posult(request):
    previous="/pos"
    try:
        xI= float(request.GET["x1"])
        yI= float(request.GET["y1"])
        aI= float(request.GET["ang1"])
        xII= float(request.GET["x2"])
        yII= float(request.GET["y2"])
        aII= float(request.GET["ang2"])

        
        aI=math.radians(int(aI))
        aII=math.radians(int(aII))
        step1= math.tan(aI)
        gr1=1/step1
        step2= math.tan(aII)
        gr2=1/step2
        mx1= gr1*xI
        c1= yI-mx1
        mx2= gr2*xII
        c2= yII-mx2
        ct= c1-c2
        mt=gr2-gr1
        x=ct/mt
        y=gr1*x
        y+=c1
        result = x,",",y
        return render(request,"result.html",{"result":result, "previous":previous})
    except:
        return render(request,"error.html",{"previous":previous})


def imc (request):
    w =  float(request.GET["w"])
    h =  float(request.GET["h"])
    h**=2
    result = w/h
    return render(request,"result.html",{"result":result,"previous":"imc"})

    
#tpor    


#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way

