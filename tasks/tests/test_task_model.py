from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task
from django.utils import timezone 
from datetime import timedelta

class TaskModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="model@test.com",
            password="pass123"
        )

    def test_create_task(self):
    
        future_date = timezone.now() + timedelta(days=7)

        task = Task.objects.create(
            title="Build API",
            description="Implement backend",
            assigned_to=self.user,
            creator=self.user,
            due_date=future_date  
        )

        self.assertEqual(task.title, "Build API")
        self.assertEqual(task.description, "Implement backend")
        self.assertEqual(task.status, "TODO")
        self.assertEqual(task.assigned_to, self.user)
        self.assertEqual(task.creator, self.user)
        self.assertIsNotNone(task.created_at)