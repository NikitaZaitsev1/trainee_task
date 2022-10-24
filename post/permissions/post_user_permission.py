from rest_framework.permissions import BasePermission, SAFE_METHODS

from innotter.enum_classes import Role, HttpMethod


class PostUserPermission(BasePermission):
    """Editing posts is restricted to the owner, admin or moderator"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.method == HttpMethod.delete:
            return request.user.role in (Role.admin, Role.moderator)

        return obj.page.owner == request.user or request.user.role == Role.admin
