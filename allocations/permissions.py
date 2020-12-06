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

methodAllocationToPerm = {
    'POST': 'add',
    'PUT': 'change',
    'PATCH': 'change',
    'DELETE': 'delete',
    'GET': 'view',
    'HEAD': 'view',
    'OPTIONS': 'view',
}

# Check if the method is one of above (methodAllocationToPerm) and check if the admin gave this permission
class IsPermittedOnPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in methodAllocationToPerm:
            return False
        return request.user.has_perm(f'allocations.{methodAllocationToPerm[request.method]}_allocation')

# DEFINITIVA
# Check if the method is one of above (methodAllocationToPerm) and check if the admin gave this permission
class IsPermittedOnPostAndPermittedAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in methodAllocationToPerm:
            return False
        return request.user.has_perm(f'allocations.{methodAllocationToPerm[request.method]}_allocation') and request.user.groups.filter(name='Students').exists()