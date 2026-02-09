from rest_framework import generics, permissions, exceptions
from django.db.models import Q
from tasks.models import Task
from .serializers import TaskSerializer
from .permissions import IsCreatorOrAssigned

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(Q(creator=user) | Q(assigned_to=user)).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsCreatorOrAssigned]
    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(Q(creator=user) | Q(assigned_to=user))

    def perform_update(self, serializer):
        user = self.request.user
        instance = self.get_object()

        if user == instance.assigned_to and user != instance.creator:
            if set(serializer.validated_data.keys()) - {'status'}:
                 raise exceptions.PermissionDenied("Assigned users can only update the status.")
        
        serializer.save()