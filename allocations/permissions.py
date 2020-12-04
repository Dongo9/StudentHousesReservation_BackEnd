import permission as permission
from rest_framework import permissions


class IsPreferenceAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.student == request.user


class IsPreferenceAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Students').exists()
