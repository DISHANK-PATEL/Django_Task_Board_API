from django.db import models
from django.conf import settings

class Task(models.Model):
   
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("DOING", "Doing"),
        ("DONE", "Done"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="assigned_tasks"
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="created_tasks"
    )

    due_date = models.DateTimeField()
    
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default="TODO"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ActivityLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Task Created'),
        ('UPDATE', 'Task Updated'),
        ('STATUS_CHANGE', 'Status Changed'),
        ('ASSIGNED', 'Task Assigned'),
        ('DELETE', 'Task Deleted'),
    ]

    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor} - {self.action} - {self.timestamp}"