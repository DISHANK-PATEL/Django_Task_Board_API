from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Task, ActivityLog
from .serializers import TaskSerializer
from .permissions import IsCreatorOrAssignee  

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users see tasks they created OR are assigned to
        return Task.objects.filter(
            Q(creator=self.request.user) | Q(assigned_to=self.request.user)
        )

    def perform_create(self, serializer):
        task = serializer.save(creator=self.request.user)
        # LOGGING
        ActivityLog.objects.create(
            actor=self.request.user,
            task=task,
            action='CREATE',
            details=f"Task '{task.title}' created."
        )

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrAssignee]

    def get_queryset(self):
        return Task.objects.filter(
            Q(creator=self.request.user) | Q(assigned_to=self.request.user)
        )

    def perform_update(self, serializer):
        # Fetch the old object to compare changes
        old_task = self.get_object()
        new_task = serializer.save()

        if old_task.status != new_task.status:
            ActivityLog.objects.create(
                actor=self.request.user,
                task=new_task,
                action='STATUS_CHANGE',
                details=f"Status changed from {old_task.status} to {new_task.status}"
            )
        elif old_task.assigned_to != new_task.assigned_to:
            assignee_name = new_task.assigned_to.email if new_task.assigned_to else "Unassigned"
            ActivityLog.objects.create(
                actor=self.request.user,
                task=new_task,
                action='ASSIGNED',
                details=f"Task assigned to {assignee_name}"
            )
        else:
            ActivityLog.objects.create(
                actor=self.request.user,
                task=new_task,
                action='UPDATE',
                details="Task details updated"
            )

    def perform_destroy(self, instance):
        ActivityLog.objects.create(
            actor=self.request.user,
            action='DELETE',
            details=f"Task '{instance.title}' was deleted."
        )
        instance.delete()

class UserTaskDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Returns tasks assigned to the current user, grouped by status.
        Structure: {"TODO": [], "DOING": [], "DONE": []}
        """
        user = request.user
        
        tasks = Task.objects.filter(assigned_to=user)
        serializer = TaskSerializer(tasks, many=True)
       
        grouped_tasks = {
            "TODO": [],
            "DOING": [],
            "DONE": []
        }

        for task_data in serializer.data:
            status = task_data.get('status')
            if status in grouped_tasks:
                grouped_tasks[status].append(task_data)
            else:
                if status not in grouped_tasks:
                    grouped_tasks[status] = [task_data]

        return Response(grouped_tasks)