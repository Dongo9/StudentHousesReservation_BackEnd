import permission as permission
from rest_framework import permissions

class IsTheCake(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employee').exists()


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and \
               not request.user.is_superuser and \
               not request.user.groups.filter(name='Employee').exists()

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
