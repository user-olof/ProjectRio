import factory
from apps.bookings.models import Booking
from tests.factories.accounts import AccountFactory
from . import accounts

from faker import Faker
fake = Faker()

class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking
    
    # event = factory.LazyAttribute(lambda _: fake.color_name())
    event = "test_lesson"
    account = factory.SubFactory(accounts.AccountFactory)
    
    def __repr__(self) -> str:
        return "Object event: " + self.event