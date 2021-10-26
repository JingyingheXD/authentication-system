import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..serializers import UserSerializer


# initialize the APIClient app
client = Client()


class SignInTest(TestCase):
    """ Test module for adding a user API  """

    def setUp(self):
        self.user_previous = {
            'username': 'hjy@gmail.com',
            'password': 'hejingying123',
        }

        self.valid_signin_user = {
            'username': 'hjy@gmail.com',
            'password': 'hejingying123',
        }

        """ blank """
        self.invalid_signin_user_no_username = {
            'username': '',
            'password': 'hejingying123',
        }
        self.invalid_signin_user_no_password = {
            'username': 'hjy@gmail.com',
            'password': '',
        }

        """ not blank """
        self.invalid_signin_nonexist_username = {
            'username': 'hjy123@gmail.com',
            'password': 'hejingying123',
        }
        self.invalid_signin_invalid_username = {
            'username': 'hjygmail.com',
            'password': 'hejingying123',
        }
        self.invalid_signin_wrong_password = {
            'username': 'hjy@gmail.com',
            'password': 'hejingying',
        }
        self.invalid_signin_invalid_password = {
            'username': 'hjy@gmail.com',
            'password': '123123',
        }

    def test_signin_valid_user(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.valid_signin_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_signin_invalid_signin_user_no_username(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_user_no_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)

    def test_signin_invalid_signin_user_no_password(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_user_no_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)

    def test_signin_invalid_signin_nonexist_username(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_nonexist_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_signin_invalid_signin_invalid_username(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_invalid_username),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_signin_invalid_signin_wrong_password(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_wrong_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)

    def test_signin_invalid_signin_invalid_password(self):
        client.post(
            reverse('users-list'),
            data=json.dumps(self.user_previous),
            content_type='application/json'
        )
        response = client.post(
            '/auth/',
            data=json.dumps(self.invalid_signin_invalid_password),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
