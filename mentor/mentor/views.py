from django.http import HttpResponse
from django.shortcuts import render
from contact.models import Contactform

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=Contactform(name=name,email=email,subject=subject,message=message)
        en.save()
    
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')

def ss(request):
    return render(request,'ss.html')

def courses(request):
    return render(request,'courses.html')

def downloads(request):
    return render(request,'downloads.html')

def bca(request):
    return render(request,'bca.html')

def bba(request):
    return render(request,'bba.html')

def ba(request):
    return render(request,'ba.html')

def bcom(request):
    return render(request,'bcom.html')

def bsc(request):
    return render(request,'bsc.html')

def ma(request):
    return render(request,'ma.html')

def mcom(request):
    return render(request,'mcom.html')

def msc(request):
    return render(request,'msc.html')

def bva(request):
    return render(request,'bva.html')

