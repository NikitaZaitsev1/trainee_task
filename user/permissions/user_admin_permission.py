from rest_framework.permissions import BasePermission, SAFE_METHODS

from innotter.enum_classes import Role


class UserAdminPermission(BasePermission):
    """Blocking users is restricted to the admin"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user.role == Role.ADMIN
