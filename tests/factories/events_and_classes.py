import factory
from apps.events_and_classes.models import EventsAndClasses
from datetime import datetime 

class EventsAndClassesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EventsAndClasses

    name = "Test lesson"
    time_length = 30
    next_event = datetime(2015, 10, 9, 23, 55, 59, 342380)
    frequency = '1w'
    address = '10 Downing Street'
    max_participants = 10
    
    def __repr__(self) -> str:
        return "Object event:" + self.name