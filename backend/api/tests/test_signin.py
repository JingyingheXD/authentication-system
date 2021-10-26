import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..serializers import UserSerializer


# initialize the APIClient app
client = Client()


class SignUpTest(TestCase):
    """ Test module for adding a user API  """

    def setUp(self):
        self.valid_user = {
            'username': 'hjy@gmail.com',
            'password': 'hejingying123',
        }

        """ blank """
        self.invalid_user_no_username = {
            'username': '',
            'password': 'hejingying123',
        }
        self.invalid_user_no_password = {
            'username': 'hjy_new@gmail.com',
            'password': '',
        }
        self.invalid_user_no_username_password = {
            'username': '',
            'password': '',
        }

    def test_add_valid_user(self):
        response = client.post(
            reverse('users-list'),
            data=json.dumps(self.valid_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_invalid_user_no_username(self):
        response = client.post(
            reverse('users-list'),
            data=json.dumps(self.invalid_user_no_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_add_invalid_user_no_password(self):
        response = client.post(
            reverse('users-list'),
            data=json.dumps(self.invalid_user_no_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_add_invalid_user_no_username_password(self):
        response = client.post(
            reverse('users-list'),
            data=json.dumps(self.invalid_user_no_username_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)

    def test_add_invalid_user_exist_username(self):
        user_previous = User.objects.create(
            username='hjy@gmail.com', password='hejingying123')
        response = client.post(
            reverse('users-list'),
            data=json.dumps(self.invalid_user_exist_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
