from rest_framework import permissions

class IsCreatorOrAssigned(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            return obj.creator == request.user

        if obj.creator == request.user:
            return True
        
        if obj.assigned_to == request.user:
            return True
            
        return False