from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'MyMems/index.html')

def productivity(request):
    return render(request,'MyMems/index.html')

def images(request):
    return HttpResponse("You are in images")

def dairy(request):
    return render(request,'MyMems/index.html')

def mistakes(request):
    return render(request,'MyMems/index.html')

def goals(request):
    return render(request,'MyMems/index.html')

def login(request):
    return render(request,'MyMems/login.html')
