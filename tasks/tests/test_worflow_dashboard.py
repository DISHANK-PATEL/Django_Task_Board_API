from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from tasks.models import Task, ActivityLog

User = get_user_model()

class TaskWorkflowTests(APITestCase):

    def setUp(self):
        self.creator = User.objects.create_user(email='creator@test.com', password='password')
        self.assignee = User.objects.create_user(email='assignee@test.com', password='password')
        self.other = User.objects.create_user(email='other@test.com', password='password')

        self.task = Task.objects.create(
            title="Test Task",
            description="Test Desc",
            creator=self.creator,
            assigned_to=self.assignee,
            status="TODO",
            due_date="2024-12-31" 
        )

    def test_dashboard_grouping(self):
        """Test if the dashboard returns tasks grouped by status"""
        self.client.force_authenticate(user=self.assignee)

        url = '/users/me/tasks/' 
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('TODO', response.data)
        self.assertIn('DONE', response.data)
        self.assertEqual(len(response.data['TODO']), 1)

    def test_only_creator_can_delete(self):
        url = reverse('task-detail', args=[self.task.id])
        
        self.client.force_authenticate(user=self.assignee)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.creator)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

    def test_activity_logging(self):
        """Test that updating status creates a log"""
        self.client.force_authenticate(user=self.assignee)
        url = reverse('task-detail', args=[self.task.id])
        
        data = {"status": "DONE"}
        self.client.patch(url, data)

        log = ActivityLog.objects.last()
        self.assertEqual(log.action, 'STATUS_CHANGE')
        self.assertEqual(log.actor, self.assignee)
        self.assertIn("TODO to DONE", log.details)