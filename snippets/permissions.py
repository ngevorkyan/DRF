from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Custom permission to only allow owners'''
    pass

