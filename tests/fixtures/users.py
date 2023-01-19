from factories.users import CustomUserFactory
import datetime, pytz

def make_objects():
    """Returns new users in testing"""
    # Default user 'John Doe'
    CustomUserFactory()
    # New user 'Anthony Hopkins'
    CustomUserFactory(
        email="anthony.hopkins@user.com",
        title='Mr',
        first_name='Anthony',
        surname='Hopkins',
        level='Medium',
        last_login=datetime.datetime(2000, 1, 1, tzinfo=pytz.UTC) ,
        password='***'
    )
