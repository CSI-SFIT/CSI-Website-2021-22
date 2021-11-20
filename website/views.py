from django.http import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')


def aboutus(request):
    return render(request,"aboutus.html")

def posts(request):
    return render(request,"posts.html")

def teams(request):
    return render(request,"teams.html")

def teams19(request):
    return render(request,"teams2019.html")

def events(request):
    return render(request,"events.html")    