from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


TOKEN_URL = reverse("token_obtain_pair")


class AuthApiTests(APITestCase):

    def setUp(self):
        self.email = "auth@test.com"
        self.password = "qwerty12345"

        self.user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

    def test_token_created_for_valid_credentials(self):
        payload = {
            "email": self.email,
            "password": self.password
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("access", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_token_not_created_invalid_password(self):
        payload = {
            "email": self.email,
            "password": "wrong"
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
