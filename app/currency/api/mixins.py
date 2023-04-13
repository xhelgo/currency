from rest_framework import permissions


class IsSuperUserMixin(permissions.BasePermission):
    # Check if the user is_superuser
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
