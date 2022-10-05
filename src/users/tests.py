from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user,com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.is_active)
        self.assertEqual(user.is_staff)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(superuser.email, 'super@user.com')
        self.assertEqual(superuser.is_active)
        self.assertEqual(superuser.is_staff)
        self.assertEqual(superuser.is_superuser)
        try:
            self.assertIsNone(superuser.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='super@user.com', password='foo', is_superuser=False)


