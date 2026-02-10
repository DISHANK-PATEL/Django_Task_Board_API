from rest_framework import permissions

class IsCreatorOrAssignee(permissions.BasePermission):
    """
    Custom permission to:
    1. Allow Creator to Delete.
    2. Allow Creator or Assignee to Update.
    3. Allow both to View.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any user involved in the task
        if request.method in permissions.SAFE_METHODS:
            return obj.creator == request.user or obj.assigned_to == request.user

        # DELETE: Only the creator can delete
        if request.method == 'DELETE':
            return obj.creator == request.user

        # UPDATE/PATCH: Creator OR Assigned user can update
        if request.method in ['PUT', 'PATCH']:
            return obj.creator == request.user or obj.assigned_to == request.user

        return False