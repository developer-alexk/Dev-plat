from django.shortcuts import render
from .models import Event,Home_Updates

def home(request):
    homes = Home_Updates.objects.all()
    return render(request,'blog/home.html',{'title':'home','homes':homes})

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

def events(request):
    event = Event.objects.all()
    return render(request,'blog/events.html',{'title':'events','event':event})