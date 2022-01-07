from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, PreviousEvent

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

def teams21(request):
    return render(request,"teams21.html")

def events(request):
    return render(request, "events.html", {"events": Event.objects.all(), "previousEvents": PreviousEvent.objects.all().order_by('-createdTime')})

def event_pages(request, event_url):
    return render(request, "events_single.html", {"event": Event.objects.get(url=event_url)})

def previous_event_pages(request, previous_event_url):
    return render(request, "previous_events_single.html", {"previousEvent": PreviousEvent.objects.get(url=previous_event_url)})

def csi_show(request):
    return render(request, "csi_show.html")
