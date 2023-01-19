from factories.bookings import BookingFactory

def make_objects():
    """ returns a new booking """
    BookingFactory()
    BookingFactory(event='volleyball')

