from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import Method
from user.models import User
from user.permissions import user_admin_permission
from user.permissions.user_admin_permission import UserAdminPermission
from user.serializers.admin_serializer import AdminSerializer
from user.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'title'

    def get_serializer_class(self):
        if self.action == Method.retrieve or self.action == Method.update:
            return AdminSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == Method.get:
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (UserAdminPermission,)
        return super(UserViewSet, self).get_permissions()
