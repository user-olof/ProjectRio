from multiprocessing import context
from django.shortcuts import render
from rioacademy.apps.events_and_classes.models import EventsAndClasses

def index(request):
    num_events_and_classes = EventsAndClasses.objects.count()
    template = 'index.html'
    # context = {}
    context = {
        'events_and_classes' : num_events_and_classes
    }

    return render(request, template, context)

    