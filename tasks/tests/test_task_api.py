from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from tasks.models import Task
from django.utils import timezone  
from datetime import timedelta     

TASK_URL = reverse("task-list")

class TaskApiTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="task@test.com",
            password="pass123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        
        future_date = timezone.now() + timedelta(days=3)

        payload = {
            "title": "API Task",
            "description": "Created via API",
            "due_date": future_date  
        }

        res = self.client.post(TASK_URL, payload)

        if res.status_code != 201:
            print(res.data) 

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        
        task = Task.objects.first()
        self.assertEqual(task.title, payload["title"])
        self.assertEqual(task.creator, self.user)