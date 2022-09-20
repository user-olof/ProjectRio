from multiprocessing import context
from django.shortcuts import render
from rest_framework import generics
from events_and_classes.models import EventsAndClasses

def index(request):
    events_and_classes = EventsAndClasses.objects.all()
    template = 'index.html'
    # context = {}
    context = {
        'events_and_classes' : events_and_classes
    }

    return render(request, template, context)

# Create your views here.
# class index(generics.GenericAPIView):
    