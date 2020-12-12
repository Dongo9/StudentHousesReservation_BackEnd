import permission as permission
from rest_framework import permissions


class IsTheCake(permissions.BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


# Check if the method is one of above (methodAllocationToPerm) and check if the admin gave this permission
class IsPermittedViewStudentsAllocations(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Administration').exists()


# Check if the method is one of above (methodAllocationToPerm) and check if the admin gave this permission
class IsPermittedOnPostAndPermittedAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Students').exists()
