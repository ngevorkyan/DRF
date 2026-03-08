from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Custom permission to only allow owners to edit'''
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to owners.
        return obj.owner == request.user        
