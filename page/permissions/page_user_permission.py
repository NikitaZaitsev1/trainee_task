from rest_framework.permissions import BasePermission, SAFE_METHODS


class PageUserPermission(BasePermission):
    """Editing pages is restricted to the owner or admin"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.role == 'admin' or request.user.role == 'moderator'
