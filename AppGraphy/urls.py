from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='AppGraphy index'),
    path("hist/",views.histogram,name="histogram"),
    path("hist/result/",views.HistResult,name='histresult'),
    path("scatter/",views.scatter,name="scatter"),
    path("scatter/result/",views.ScatterResult,name='scatterresult'),
    path("bar/",views.bar,name="{{bar}}"),
    path("bar/result/",views.BarResult,name='barresult'),
    path("pie/",views.pie,name="pie"),
    path("pie/result/",views.PieResult,name='pieresult'),
    path("3d-scatter/",views.scatter3D,name="3dscatter"),
    path("3d-scatter/result/",views.Scatter3Dresult,name='3dscatterresult'),
    path("steam/",views.steam,name="steam"),
    path("steam/result/",views.steamresult,name='steamresult'),
    
    path("step/",views.step,name="step"),
    path("step/result/",views.stepresult,name='stepresult'),
    
    path("line/",views.line,name="line"),
    path("line/result/",views.lineresult,name='lineresult'),

    path("contact/",views.contact,name='contact'),
    path("about/",views.about,name='about'),

    path('3d-scatter/help/',views.helpS3d,name='help'),
    path('bar/help/',views.helpbar,name='help'),
    path('hist/help/',views.helphist,name='hist'),
    path('step/help/',views.helpstep,name='step'),
    path('line/help/',views.helpline,name='help'),
    path('pie/help/',views.helppie,name='help'),
    path('scatter/help/',views.helpscatter,name='help'),
    path('steam/help/',views.helpsteam,name='help'),





]