from django.urls import path
from .views import TaskListCreateView, TaskDetailView, UserTaskDashboardView

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path('dashboard/', UserTaskDashboardView.as_view(), name='task-dashboard'),
]