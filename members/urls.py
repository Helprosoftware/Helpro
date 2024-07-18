from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('maths/', views.members, name='members'),
#gauss forms
    path('gauss/', views.gausso, name='gauss'),
    path('gauss_/', views.gauss_, name='gauss_'),
    path('gaus_s/',views.gaus_s, name="gaus_s"),
    path('intervalo',views.intervalo,name="inter"),
#gauss results
    path('results/',views.gaussear, name='results'),
    path('results_/',views.gaussear_, name='results'),
    path('result_s/',views.gaussea_r,name='gaussea_r'),
    path('resultinter/',views.inter,name="resultinter"),
#parallelogramo forms y result
    path('parall/', views.parall, name="parall"),
    path('parasult/',views.parasult, name="parasult"),
#3d pythagoras
    path('3d/', views.td, name="3d"),
    path('3dsult/',views.tdsult, name="3dsult"),
#distance between point and line plus triangle data
    path('dist/', views.distpl, name= "dist"),
    path('dpl/', views.dpl, name= "dpl"),
#triangleinfo
    path('triang/',views.triang, name="triang"),
    path('tri/',views.tri,name="tri"),
    path("angul/", views.angul, name = "angul"),
#symetry
    path('sym/',views.simp, name = "sym" ),
    path('simpo/',views.simpo, name = "simpo" ),
    path('siml/',views.siml, name = "simlo"),
    path('simlo/',views.simlo,name = "simlo"),
#circles
    path("circ/",views.circ,name = "circ"),
    path("circo/",views.circo,name = "circo"),
    path("circ3/", views.circ3, name = "circ3"),
    path("circ3o/",views.circ3o,name = "circ3o"),
    path("circpl/", views.circpl, name = "circpl"),
    path("circplo/", views.circplo, name = "circplo"),
    path("circd/",views.circd, name = "circd"),
    path("circdo/",views.circdo, name = "circdo"),
#plotrr
    #path("plotrr/",views.plotrrrot, name = "plotrr"),
    #path("plotrrot/",views.plotrr, name ="plotrrrot"),
    #path("plotrrot1/",views.plotrrot1, name ="plotrrrot1"),
    #path("plot1/",views.plot1, name ="plot1"),
#matriz
    path("matriz/",views.matriz, name = "matriz"),
    path("det3/",views.det3, name = "det3"),
    path("matriz4/",views.matriz4, name = "matriz4"),
    path("det4/",views.det4, name = "det4"),
    path("matriz5/",views.matriz5, name = "matriz5"),
    path("det5/",views.det5, name = "det5"),
#triangulacion
    path("pos/",views.pos, name = "pos"),
    path("posult/",views.posult, name = "posult"),
    
]
