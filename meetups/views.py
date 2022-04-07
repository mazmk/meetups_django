from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    meetups = [
        {"title": "First meetup"},
        {"title": "Second meetup"},
        {"title": "Third meetup"},
    ]
    return render(request, 'meetups/index.html', {"meetups": meetups})
