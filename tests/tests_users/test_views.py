from django.test import TestCase
import unittest
from unittest.mock import patch
from tests.fixtures import users
from apps.users.models import CustomUser


class UserViewTests(TestCase):
    def setUp(self):
        users.make_objects()

    def test_retrieve_user(self):
        response = self.client.get('/home/accounts/1/')
        self.assertEqual(response.status_code, 200)

