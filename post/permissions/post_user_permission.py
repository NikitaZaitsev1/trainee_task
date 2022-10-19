from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserPermission(BasePermission):
    """Editing posts is restricted to the owner, admin or moderator"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            return request.user.role == 'admin' or request.user.role == 'moderator'

        return obj.page.owner == request.user or request.user.role == 'admin'
