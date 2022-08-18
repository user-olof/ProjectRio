from django.test import TestCase
from django.test import Client
 
# Create your tests here.
from bookings.models import Member
class BookingsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        c = Client()
        response = c.post('/localhost/')
        response.status_code        

    class GetOneMember(TestCase):
        def setUp(self):
            Member.objects.create(
                title="Mrs",
                first_name="Molly",
                surname="Holmes",
                level="Beginner",
                last_login=""
                )

    