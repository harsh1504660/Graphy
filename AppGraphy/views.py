from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style
import random as rd
import numpy as np
from django.contrib import messages

def index(request):
    return render(request,'home.html')


def HistResult(request):   
    try :
        x_var=request.POST.get('x var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')
        plt.style.use(bg)

        x = list(map(int,x_var.strip().split()))
        fig, ax = plt.subplots()  # Create a figure containing a single axes.
        ax.hist(x,color=colour)  # Plot some data on the axes.
        plt.title(head)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-Histogram'}
        return render(request,'result.html',params)
    except : 
       return render(request,'error.html')
def histogram(request):
    return render(request,'hist.html')


def scatter(request):
    return render(request,'scatterplot.html')
def ScatterResult(request):
    try:
        messages.success(request,'welcome')
        x_var=request.POST.get('x var','default')
        y_var=request.POST.get('y var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')
        
        x = list(map(int,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        n=len(x)

        fig,ax = plt.subplots()
        if colour=='difrent':
             color=['r','b','y','g','indigo','lightgreen','lightblue','orange','brown']
             
             color = rd.sample(color,n)
             ax.scatter(x, y,c=color)
        else:
             ax.scatter(x,y,color=colour)

        plt.style.use(bg)
        plt.title(head)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-Scatter'}
        return render(request,'result.html',params)
    except:
       return render(request,'error.html')
    

def bar(request):
    return render(request,'bar.html')
def BarResult(request):
    try:
        x_var=request.POST.get('x var','default')
        y_var=request.POST.get('y var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')
        
        x = list(map(str,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        n=len(y)

        fig,ax = plt.subplots()
        if colour=='difrent':
             color=['r','b','y','g','indigo','lightgreen','lightblue','orange','brown']
             
             color = rd.sample(color,n)
             ax.bar(x,y, width=1, edgecolor="white", linewidth=0.7,color=color)
        else:
            ax.bar(x,y, width=1, edgecolor="white", linewidth=0.7, color=colour)

        plt.style.use(bg)
        plt.title(head)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-Bar'}
        return render(request,'result.html',params)
    except:
        return render(request,'error.html')
    

def pie(request):
        return render(request,'pie.html')
def PieResult(request):
    try:
        x_var=request.POST.get('x var','default')
        x_label=request.POST.get('label','default')
        colour = request.POST.get('colour','default')
        x = list(map(int,x_var.strip().split()))
        label = list(map(str,x_label.strip().split()))

        if colour=='difrent':
            plt.pie(x,labels = label)
            plt.savefig('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
            return render(request,'result.html')
        else:
            colors = plt.get_cmap(colour)(np.linspace(0.2, 0.7, len(x)))
            plt.pie(x,labels = label,colors=colors)
            plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
            params={'title':'Result-Pie'}
            return render(request,'result.html',params)
    
    except:
       return render(request,'error.html')
    

def scatter3D(request):
    return render(request,'3dscatter.html')
def Scatter3Dresult(request):
    try:
        x_var=request.POST.get('x var','default')
        y_var=request.POST.get('y var','default')
        z_var=request.POST.get('z var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        z_label=request.POST.get('z label','deafult')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')

        x = list(map(int,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        z = list(map(int,z_var.strip().split()))
        n=len(x)
        
        fig = plt.figure(figsize = (10, 7))
        ax = plt.axes(projection ="3d")

        if colour=='difrent':
            color=['r','b','y','g','indigo','lightgreen','lightblue','orange','brown']
             
            color = rd.sample(color,n)
            ax.scatter(x, y,c=color)
        else:
            ax.scatter(x, y, z,color=colour)
        ax.set_xlabel(x_label, fontweight ='bold')
        ax.set_ylabel(y_label, fontweight ='bold')
        ax.set_zlabel(z_label, fontweight ='bold')
        plt.title(head)
        plt.style.use(bg)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-S3D'}
        return render(request,'result.html',params)
    except:
        return render(request,'error.html')


def steamresult(request):
    try:
        x_var = request.POST.get('x var','default')
        y_var = request.POST.get('y var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')

        x = list(map(int,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        plt.style.use(bg)
        fig, ax = plt.subplots()
        ax.stem(x, y,linefmt=colour)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(head)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-StemPlot'}
        return render(request,'result.html',params)
    except:
        return render(request,'error.html')
def steam(request):
    return render(request,'steam.html')


def step(request):
    return render(request,'step.html')
def stepresult(request):
    try :
        x_var = request.POST.get('x var','default')
        y_var = request.POST.get('y var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')

        x = list(map(int,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        fig, ax = plt.subplots()
        ax.step(x, y, linewidth=2.5,color=colour)

        plt.style.use(bg)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(head)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-StepPlot'}
        return render(request,'result.html',params)
    except:
        return render(request,'error.html')


def line(request):
    return render(request,'line.html')
def lineresult(request):
    try:    
        x_var = request.POST.get('x var','default')
        y_var = request.POST.get('y var','default')
        x_label=request.POST.get('x label','x axis')
        y_label=request.POST.get('y label','y axis')
        colour=request.POST.get('colour','blue')
        head=request.POST.get('title','TITLE')
        bg=request.POST.get('bgtheme','_classic_test_patch')

        x = list(map(int,x_var.strip().split()))
        y = list(map(int,y_var.strip().split()))
        fig, ax = plt.subplots()
        ax.plot(x, y,color=colour)

        plt.style.use(bg)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(head)
        plt.savefig('E:/django/PROJECTS/project-2/Graphy/AppGraphy/static/AppGraphy/123.png')
        params={'title':'Result-LinePlot'}
        return render(request,'result.html',params)
    except:
        return render(request,'error.html')


def about(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/about.txt')
    content=f.read()
    params={'content':content}
    return render(request,'about.html',params)

def contact(request):
    return render(request,'contact.html')


def helpS3d(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/help3DS.txt')
    content=f.read()
    params={'title':'S3D-Help','content':content}
    return render(request,'help.html',params)
def helpbar(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helpbar.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helphist(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helphist.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helpline(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helpline.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helppie(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helppie.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helpscatter(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/help2ds.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helpsteam(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helpsteam.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)
def helpstep(request):
    f=open('D:/harsh/django/PROJECTS/project-2/Graphy/AppGraphy/texts/helpstep.txt')
    content=f.read()
    params={'title':'bar-Help','content':content}
    return render(request,'help.html',params)


