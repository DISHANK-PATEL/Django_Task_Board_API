from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from tasks.models import Task


TASK_URL = reverse("task-list")


def auth_client(client, user):
    token = RefreshToken.for_user(user)
    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token.access_token}"
    )
    return client


class TaskApiTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="task@test.com",
            password="qwerty123"
        )
        self.client = auth_client(self.client, self.user)

    def test_create_task(self):
        payload = {
            "title": "API Task",
            "description": "Created via API"
        }

        res = self.client.post(TASK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
