from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        # with self.assertRaises(TypeError):
        #     User.objects.create_user()
        # with self.assertRaises(TypeError):
        #     User.objects.create_user(email='')
        # with self.assertRaises(TypeError):
        #     User.objects.create_user(email='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email='test@user.com', password='foo')
        self.assertEqual(superuser.email, 'test@user.com')
        self.assertEqual(superuser.is_active, True)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_superuser, True)
        try:
            self.assertIsNone(superuser.username)
        except AttributeError:
            pass
        # with self.assertRaises(ValueError):
        #     User.objects.create_superuser(email='test@user.com', password='foo', is_superuser=False)

    def test_creating_new_instance(self):
        User = get_user_model()
        new_user = User.objects.create_user(email="new@user.com", password="***")



