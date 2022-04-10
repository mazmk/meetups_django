from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.


def index(request):
    meet = Meetup.objects.all()
    return render(request, 'meetups/index.html', {"meetups": meet})


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetups_details.html', {'meetup_found':True,"meetups": selected_meetup})
    except Exception as exc:
        return render(request, 'meetups/meetups_details.html', {'meetup_found':False, 'exc': exc})

