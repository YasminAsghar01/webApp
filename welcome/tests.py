# social/tests.py

from django.test import TestCase
from django.contrib import auth

from welcome.models import User

TEST_USERNAME = 'samira'
TEST_PASSWORD = 'password123'


class UserTestCase(TestCase):

    def setUp(self):
        samira = User.objects.create(username=TEST_USERNAME)
        samira.set_password(TEST_PASSWORD)
        # need to save after setting password
        samira.save()

    def test_users_count(self):
        """Check that we have 1 user in test DB"""

        n_users = User.objects.all().count()
        self.assertEqual(n_users, 1)

    def test_samira_password_set(self):
        """Check that password for user samira has been set"""

        user = auth.authenticate(
            username=TEST_USERNAME, password=TEST_PASSWORD)
        self.assertIsNotNone(user)
