from django.shortcuts import render
from .models import Video,Link

def homeacademia(request):
    videos = Video.objects.all()
    link = Link.objects.all()
    return render(request,'academia/homeacademia.html',{'videos':videos,'link':link})


def djangotuto(request):
    return render(request,'academia/django.html')    