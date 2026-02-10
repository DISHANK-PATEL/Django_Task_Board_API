from django.contrib import admin
from .models import Task, ActivityLog

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
 
    list_display = ('id', 'title', 'status', 'creator', 'assigned_to', 'due_date')

    list_filter = ('status', 'due_date', 'creator', 'assigned_to')
   
    search_fields = ('title', 'description', 'creator__email', 'assigned_to__email')
    
    fieldsets = (
        ('Task Info', {
            'fields': ('title', 'description', 'status', 'due_date')
        }),
        ('Assignments', {
            'fields': ('creator', 'assigned_to')
        }),
    )

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    
    list_display = ('timestamp', 'actor', 'action', 'get_task_link', 'details')

    list_filter = ('action', 'timestamp', 'actor')

    search_fields = ('details', 'actor__email', 'task__title')

    readonly_fields = ('timestamp', 'actor', 'action', 'task', 'details')

    def get_task_link(self, obj):
        if obj.task:
            return obj.task.title
        return "Deleted Task"
    get_task_link.short_description = "Related Task"