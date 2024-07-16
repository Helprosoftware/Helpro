#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
#This software is licensed under the GNU General Public License version 3 (GPL), please read it if ussing this code in any way
from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse
import math
from random import *
ptable={"H":1,"He":4,"Li":6.94,"Be":9,"B":10.8,"C":12,"N":14,"O":16,"F":19,"Ne":20.18,"Na":23,"Mg":24.31 ,"Al":27,"Si":28.09,"P":31,"S":32.07,"Cl":35.45,"Ar":39.95,"K":39.1,"Ca":40.08,"Sc":44.96,"Ti":47.87,"V":50.94,"Cr":52,"Mn":54.94,"Fe":55.85,"Co":58.933,"Ni":58.693,"Cu":63.54,"Zn":65.38,"Ga":69.723,"Ge":74.92,"Se":79,"Br":80,"Kr":83.8,"Rb":85.47,"Sr":87.62,"Y":88.9,"Zr":91.224,"Nb":92.9,"Mo":95.95,"Tc":98,"Ru":101,"Rh":102.91,"Pd":106.4,"Ag":107.87,"Cd":112.4,"In":114.82,"Sn":118.71,"Sb":121.76,"Te":127.6,"I":126.9,"Xe":131.29,"Cs":132.91,"Ba":137.33,"Hf":178.49,"Ta":180.95,"W":183.84,"Re":186.21,"Os":190.23,"Ir":192.22,"Pt":195,"Au":196,"Hg":200.6,"Tl":204.38,"Pb":207.2,"Bi":208.98,"Po":209,"At":210,"Rn":222,"Fr":223,"Ra":226,"Rf":267,"Db":268,"Sg":269,"Bh":270,"Hs":277}
#this decifind function MUST NOT be used outside this program, as it rounds 0.4 aandd 0.6 to 0.5
def decifind(x):
    xr=math.trunc(x)
    x=round(x,1)
    if x+0.8==xr+1:
        dec=0.2
    elif x+0.7==xr+1:
        dec=0.3
    elif x+0.6==xr+1:
        dec=0.5
    elif x+0.5==xr+1:
        dec=0.5
    elif x+0.4==xr+1:
        dec=0.5
    elif x+0.3==xr+1:
        dec=0.7
    elif x+0.2==xr+1:
        dec=0.8
    elif x+1==xr+1 or x+0.9== xr+1:
        dec=0
    elif x+0.1==xr+1 or x==xr+1:
        dec=1
    
    return(dec)

def chem(request):
    
    return render(request,"chem.html",{})

def mr2(request):
    return render(request,"mr2.html",{})
def mr3(request):
    return render(request,"mr3.html",{})
def mr4(request):
    return render(request,"mr4.html",{})


#def question (request):
    #title="calculating empirical formula with 2 elements"
    #p2= randint(1,100)
    #p1= 100-p2
    #Ar1=
    #Ar2=
    #qn= randint(1,2)

    #if qn == 1:
      #  question= " bobby has element with Ar",Ar1
    #elif qn == 2:
     #   question= " tommy has element with ar ",Ar1
    #paraf = p1,p2
    #return render(request,"questiongo.html",{"title":title, "question":question})
    
    

def prom2(e1,p1,e2,p2):
    
    Ar1=ptable[e1]
    
    
    Ar2=ptable[e2]
    
    #so, now step one is equal to percentage over Ar
    el1=p1/Ar1
    el2=p2/Ar2
    milist=[el1,el2]
    mini=min(milist)
    el1=el1/mini
    el2=el2/mini
    d1=decifind(el1)
    d2=decifind(el2)
    if d1==0.2 or d2==0.2:
        el1=el1*5
        el2=el2*5
    elif d1==0.3 or d2==0.3:
        el1=el1*3
        el2=el2*3
    elif d1==0.5 or d2==0.5:
        el1=el1*2
        el2=el2*2
    elif d1==0.7 or d2==0.7:
        el1=el1*1.4
        el2=el2*1.4
    elif d1==0.8 or d2==0.8:
        el1=el1*1.25
        el2=el2*1.25
    el1=round(el1)
    el2=round(el2)
    result=e1,el1,"and",e2,el2
    return(result)
    

def prom3(e1,p1,e2,p2,e3,p3):
    Ar1=ptable[e1]
    Ar2=ptable[e2]
    Ar3=ptable[e3]
    
    #so, now step one is equal to percentage over Ar...
    el1=p1/Ar1
    el2=p2/Ar2
    el3=p3/Ar3
    milist=[el1,el2,el3]
    mini=min(milist)
    el1=el1/mini
    el2=el2/mini
    el3=el3/mini
    d1=decifind(el1)
    d2=decifind(el2)
    d3=decifind(el3)
    if d1==0.2 or d2==0.2 or d3==0.2:
        el1=el1*5
        el2=el2*5
        el3=el3*5
    elif d1==0.3 or d2==0.3 or d3==0.3:
        el1=el1*3
        el2=el2*3
        el3=el3*3
    elif d1==0.5 or d2==0.5 or d3==0.5:
        el1=el1*2
        el2=el2*2
        el3=el3*2
    elif d1==0.7 or d2==0.7 or d3==0.7:
        el1=el1*1.4
        el2=el2*1.4
        el3=el3*1.4
    elif d1==0.8 or d2==0.8 or d3==0.8:
        el1=el1*1.25
        el2=el2*1.25
        el3=el3*1.25
    el1=round(el1)
    el2=round(el2)
    el3=round(el3)
    result=e1,el1,"and",e2,el2,"and",e3,el3
    return(result)
#DOESNT WsORK
def promr2(request):
    
        e1=request.GET["e1"]
        
        p1=request.GET["p1"]
        p1=float(p1)
        e2=request.GET["e2"]
        
        p2=request.GET["p2"]
        p2=float(p2)
        #so, now step one is equal to percentage over Ar
        result = prom2(e1,p1,e2,p2)
        previous="/mr2"
        return render(request,"result.html",{"result":result,"previous":previous})
    
        
def promr3(request):
    #getting data and A r from table...
    
    e1=request.GET["e1"]
    
    p1=request.GET["p1"]
    p1=float(p1)
    e2=request.GET["e2"]
    
    p2=request.GET["p2"]
    p2=float(p2)
    e3=request.GET["e3"]

    p3=request.GET["p3"]
    p3=float(p3)
    #so, now step one is equal to percentage over Ar...
    result = prom3(e1,p1,e2,p2,e3,p3)
    previous="/mr3"
    return render(request,"result.html",{"result":result,"previous":previous})
    
        
    
    
def promr4(request):
    #getting data and A r from table...
    
    e1=request.GET["e1"]
    Ar1=ptable[e1]
    p1=request.GET["p1"]
    p1=float(p1)
    e2=request.GET["e2"]
    Ar2=ptable[e2]
    p2=request.GET["p2"]
    p2=float(p2)
    e3=request.GET["e3"]
    Ar3=ptable[e3]
    p3=request.GET["p3"]
    p3=float(p3)
    e4=request.GET["e4"]
    Ar4=ptable[e4]
    p4=request.GET["p4"]
    p4=float(p4)
    #so, now step one is equal to percentage over Ar...
    el1=p1/Ar1
    el2=p2/Ar2
    el3=p3/Ar3
    el4=p4/Ar4
    milist=[el1,el2,el3]
    mini=min(milist)
    el1=el1/mini
    el2=el2/mini
    el3=el3/mini
    el4=el4/mini
    d1=decifind(el1)
    d2=decifind(el2)
    d3=decifind(el3)
    d4=decifind(el4)
    if d1==0.2 or d2==0.2 or d3==0.2 or d4==0.2:
        el1=el1*5
        el2=el2*5
        el3=el3*5
        el4=el4*5
    elif d1==0.3 or d2==0.3 or d3==0.3 or d4==0.3:
        el1=el1*3
        el2=el2*3
        el3=el3*3
        el4=el4*3
    elif d1==0.5 or d2==0.5 or d3==0.5 or d4==0.5:
        el1=el1*2
        el2=el2*2
        el3=el3*2
        el4=el4*2
    elif d1==0.7 or d2==0.7 or d3==0.7 or d4==0.7:
        el1=el1*1.4
        el2=el2*1.4
        el3=el3*1.4
        el4=el4*1.4
    elif d1==0.8 or d2==0.8 or d3==0.8 or d4==0.8:
        el1=el1*1.25
        el2=el2*1.25
        el3=el3*1.25
        el4=el4*1.25
    el1=round(el1)
    el2=round(el2)
    el3=round(el3)
    el4=round(el4)
    result=e1,el1,"and",e2,el2,"and",e3,el3,"and",e4,el4
    previous="/mr4"
    return render(request,"result.html",{"result":result,"previous":previous})   
 
         
        

def molec2(request):
    return render(request,"molec2.html",{})

def molec3(request):
    return render(request,"molec3.html",{})

def molec4(request):
    return render(request,"molec4.html",{})

def molec2tvm(request):
    return render(request,"molec2tvm.html",{})

def molec3tvm(request):
    return render(request,"molec3tvm.html",{})

def molec4tvm(request):
    return render(request,"molec4tvm.html",{})

def molecsult2(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)
        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)
        Mr=request.GET["Mr"]
        Mr=float(Mr)
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        milist=[el1,el2]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        d1=decifind(el1)
        d2=decifind(el2)
        if d1==0.2 or d2==0.2:
            el1=el1*5
            el2=el2*5
        elif d1==0.3 or d2==0.3:
            el1=el1*3
            el2=el2*3
        elif d1==0.5 or d2==0.5:
            el1=el1*2
            el2=el2*2
        elif d1==0.7 or d2==0.7:
            el1=el1*1.4
            el2=el2*1.4
        elif d1==0.8 or d2==0.8:
            el1=el1*1.25
            el2=el2*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        Ar1*=empel1
        Ar2*=empel2
        
        mr=Ar1+Ar2
        ratio=round(Mr/mr)
        
        el1=empel1*ratio
        el2=empel2*ratio
        result=e1,empel1,"and",e2,empel2,".........molecular:",e1,round(el1),"and",e2,round(el2)
        previous="/molec2"
        return render(request,"result.html",{"result":result,"previous":previous})
        
    
def molecsult3(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)
        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)
        e3=request.GET["e3"]
        Ar3=ptable[e3]
        p3=request.GET["p3"]
        p3=float(p3)
        Mr=request.GET["Mr"]
        Mr=float(Mr)
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        el3=p3/Ar3
        milist=[el1,el2,el3]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        el3=el3/mini
        d1=decifind(el1)
        d2=decifind(el2)
        d3=decifind(el3)
        if d1==0.2 or d2==0.2 or d3==0.2:
            el1=el1*5
            el2=el2*5
            el3=el3*5
        elif d1==0.3 or d2==0.3 or d3==0.3:
            el1=el1*3
            el2=el2*3
            el3=el3*3
        elif d1==0.5 or d2==0.5 or d3==0.5:
            el1=el1*2
            el2=el2*2
            el3=el3*2
        elif d1==0.7 or d2==0.7 or d3==0.7:
            el1=el1*1.4
            el2=el2*1.4
            el3=el3*1.4
        elif d1==0.8 or d2==0.8 or d3==0.8:
            el1=el1*1.25
            el2=el2*1.25
            el3=el3*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        empel3=round(el3)
        
        Ar1*=empel1
        Ar2*=empel2
        Ar3*=empel3
        
        mr=Ar1+Ar2+Ar3
        ratio=round(Mr/mr)
        
        el1=empel1*ratio
        el2=empel2*ratio
        el3=empel3*ratio
        result=e1,empel1,"and",e2,empel2,"and",e3,empel3,".........molecular:",e1,round(el1),"and",e2,round(el2),"and",e3,round(el3),
        previous="/molec3"
        return render(request,"result.html",{"result":result,"previous":previous})


def molecsult4(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)

        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)

        e3=request.GET["e3"]
        Ar3=ptable[e3]
        p3=request.GET["p3"]
        p3=float(p3)

        e4=request.GET["e4"]
        Ar4=ptable[e4]
        p4=request.GET["p4"]
        p4=float(p4)

        Mr=request.GET["Mr"]
        Mr=float(Mr)
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        el3=p3/Ar3
        el4=p4/Ar4
        milist=[el1,el2,el3,el4]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        el3=el3/mini
        el4=el4/mini
        d1=decifind(el1)
        d2=decifind(el2)
        d3=decifind(el3)
        d4=decifind(el4)
        if d1==0.2 or d2==0.2 or d3==0.2 or d4==0.2:
            el1=el1*5
            el2=el2*5
            el3=el3*5
            el4=el4*5
        elif d1==0.3 or d2==0.3 or d3==0.3 or d4==0.3:
            el1=el1*3
            el2=el2*3
            el3=el3*3
            el4=el4*3
        elif d1==0.5 or d2==0.5 or d3==0.5 or d4==0.5:
            el1=el1*2
            el2=el2*2
            el3=el3*2
            el4=el4*2
        elif d1==0.7 or d2==0.7 or d3==0.7 or d4==0.7:
            el1=el1*1.4
            el2=el2*1.4
            el3=el3*1.4
            el4=el4*1.4
        elif d1==0.8 or d2==0.8 or d3==0.8 or d4==0.8:
            el1=el1*1.25
            el2=el2*1.25
            el3=el3*1.25
            el4=el4*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        empel3=round(el3)
        empel4=round(el4)
        Ar1*=empel1
        Ar2*=empel2
        Ar3*=empel3
        Ar4*=empel4
        mr=Ar1+Ar2+Ar3+Ar4
        ratio=round(Mr/mr)
        
        el1=empel1*ratio
        el2=empel2*ratio
        el3=empel3*ratio
        el4=empel4*ratio
        result=e1,empel1,"and",e2,empel2,"and",e3,empel3,"and",e4,empel4,".........molecular:",e1,round(el1),"and",e2,round(el2),"and",e3,round(el3),"and",e4,round(el4)
        previous="/molec4"
        return render(request,"result.html",{"result":result,"previous":previous})
def molecsult2tvm(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)
        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)

        v=float(request.GET["v"])
        
        t=float(request.GET["t"])
        p1=float(p1)
        M=float(request.GET["M"])
        
        p=float(request.GET["p"])

        d=M/v
        r=0.082
       
        Mr=d*r*t/p
        
        
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        milist=[el1,el2]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        d1=decifind(el1)
        d2=decifind(el2)
        if d1==0.2 or d2==0.2:
            el1=el1*5
            el2=el2*5
        elif d1==0.3 or d2==0.3:
            el1=el1*3
            el2=el2*3
        elif d1==0.5 or d2==0.5:
            el1=el1*2
            el2=el2*2
        elif d1==0.7 or d2==0.7:
            el1=el1*1.4
            el2=el2*1.4
        elif d1==0.8 or d2==0.8:
            el1=el1*1.25
            el2=el2*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        Ar1*=empel1
        Ar2*=empel2
        
        mr=Ar1+Ar2
        ratio=round(Mr/mr)
        
        
        el1=empel1*ratio
        el2=empel2*ratio
        result=e1,empel1,"and",e2,empel2,".........molecular:",e1,round(el1),"and",e2,round(el2)
        previous="/molec2tvm"
        return render(request,"result.html",{"result":result,"previous":previous})
def molecsult3tvm(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)
        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)
        e3=request.GET["e3"]
        Ar3=ptable[e3]
        p3=request.GET["p3"]
        p3=float(p3)

        v=float(request.GET["v"])
        
        t=float(request.GET["t"])
        p1=float(p1)
        M=float(request.GET["M"])
        
        p=float(request.GET["p"])

        d=M/v
        r=0.082
       
        Mr=d*r*t/p
        
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        el3=p3/Ar3
        milist=[el1,el2,el3]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        el3=el3/mini
        d1=decifind(el1)
        d2=decifind(el2)
        d3=decifind(el3)
        if d1==0.2 or d2==0.2 or d3==0.2:
            el1=el1*5
            el2=el2*5
            el3=el3*5
        elif d1==0.3 or d2==0.3 or d3==0.3:
            el1=el1*3
            el2=el2*3
            el3=el3*3
        elif d1==0.5 or d2==0.5 or d3==0.5:
            el1=el1*2
            el2=el2*2
            el3=el3*2
        elif d1==0.7 or d2==0.7 or d3==0.7:
            el1=el1*1.4
            el2=el2*1.4
            el3=el3*1.4
        elif d1==0.8 or d2==0.8 or d3==0.8:
            el1=el1*1.25
            el2=el2*1.25
            el3=el3*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        empel3=round(el3)
        Ar1*=empel1
        Ar2*=empel2
        Ar3*=empel3
        
        mr=Ar1+Ar2+Ar3
        ratio=round(Mr/mr)
        
        
        
        el1=empel1*ratio
        el2=empel2*ratio
        el3=empel3*ratio
        result=e1,empel1,"and",e2,empel2,"and",e3,empel3,".........molecular:",e1,round(el1),"and",e2,round(el2),"and",e3,round(el3),
        previous="/molec3tvm"
        return render(request,"result.html",{"result":result,"previous":previous})
def molecsult4tvm(request):
    
        e1=request.GET["e1"]
        Ar1=ptable[e1]
        p1=request.GET["p1"]
        p1=float(p1)

        e2=request.GET["e2"]
        Ar2=ptable[e2]
        p2=request.GET["p2"]
        p2=float(p2)

        e3=request.GET["e3"]
        Ar3=ptable[e3]
        p3=request.GET["p3"]
        p3=float(p3)

        e4=request.GET["e4"]
        Ar4=ptable[e4]
        p4=request.GET["p4"]
        p4=float(p4)

        v=float(request.GET["v"])
        
        t=float(request.GET["t"])
        p1=float(p1)
        M=float(request.GET["M"])
        
        p=float(request.GET["p"])

        d=M/v
        r=0.082
       
        Mr=d*r*t
        Mr/=p

        
        #so, now step one is equal to percentage over Ar
        el1=p1/Ar1
        el2=p2/Ar2
        el3=p3/Ar3
        el4=p4/Ar4
        milist=[el1,el2,el3,el4]
        mini=min(milist)
        el1=el1/mini
        el2=el2/mini
        el3=el3/mini
        el4=el4/mini
        d1=decifind(el1)
        d2=decifind(el2)
        d3=decifind(el3)
        d4=decifind(el4)
        if d1==0.2 or d2==0.2 or d3==0.2 or d4==0.2:
            el1=el1*5
            el2=el2*5
            el3=el3*5
            el4=el4*5
        elif d1==0.3 or d2==0.3 or d3==0.3 or d4==0.3:
            el1=el1*3
            el2=el2*3
            el3=el3*3
            el4=el4*3
        elif d1==0.5 or d2==0.5 or d3==0.5 or d4==0.5:
            el1=el1*2
            el2=el2*2
            el3=el3*2
            el4=el4*2
        elif d1==0.7 or d2==0.7 or d3==0.7 or d4==0.7:
            el1=el1*1.4
            el2=el2*1.4
            el3=el3*1.4
            el4=el4*1.4
        elif d1==0.8 or d2==0.8 or d3==0.8 or d4==0.8:
            el1=el1*1.25
            el2=el2*1.25
            el3=el3*1.25
            el4=el4*1.25

        
        empel1=round(el1)
        empel2=round(el2)
        empel3=round(el3)
        empel4=round(el4)
        Ar1*=empel1
        Ar2*=empel2
        Ar3*=empel3
        Ar4*=empel4
        mr=Ar1+Ar2+Ar3+Ar4
        ratio=round(Mr/mr)
        
        el1=empel1*ratio
        el2=empel2*ratio
        el3=empel3*ratio
        el4=empel4*ratio
        result="1",Ar1,"2",Ar2,"3",Ar3,"4",Ar4,ratio,e1,empel1,"and",e2,empel2,"and",e3,empel3,"and",e4,empel4,".........molecular:",e1,round(el1),"and",e2,round(el2),"and",e3,round(el3),"and",e4,round(el4)
        previous="/molec4"
        return render(request,"result.html",{"result":result,"previous":previous})

# Create your views here.
