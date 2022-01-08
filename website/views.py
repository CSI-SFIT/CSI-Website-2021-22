from django.http import response,Http404
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
    if Event.objects.filter(url=event_url).exists():
        return render(request, "events_single.html", {"event": Event.objects.get(url=event_url)})
    else:
        raise Http404("No such Event exists")

def previous_event_pages(request, previous_event_url):
    if PreviousEvent.objects.filter(url=previous_event_url).exists():
        return render(request, "previous_events_single.html", {"previousEvent": PreviousEvent.objects.get(url=previous_event_url)})
    else:
        raise Http404("No such Previous Event exists")

def csi_show(request):
    return render(request, "csi_show.html")

def magazines(request):
    return render(request, "magazines.html")

def handler404(request,exception):
    return render(request, "404.html", status=404)

def magazines_single(request,year):
    if year not in [2018,2019,2020]:
        raise Http404("Wrong Year for Magazine")
    else:
        return render(request, "magazine_single.html",{"year":year})
