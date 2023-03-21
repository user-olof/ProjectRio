import factory
from apps.bookings.models import Booking
from tests.factories.accounts import AccountFactory
from . import accounts, events_and_classes

from faker import Faker
fake = Faker()

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking
    
    # event = factory.LazyAttribute(lambda _: fake.color_name())
    event = factory.SubFactory(events_and_classes.EventsAndClassesFactory)
    account = factory.SubFactory(accounts.AccountFactory)
    
    def __repr__(self) -> str:
        return "Object event: " + self.event