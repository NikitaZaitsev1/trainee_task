from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import HttpMethod
from user.models import User
from user.permissions import user_admin_permission
from user.permissions.user_admin_permission import UserAdminPermission
from user.serializers.admin_serializer import AdminSerializer
from user.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'title'

    def get_serializer_class(self):
        if self.action == HttpMethod.retrieve or self.action == HttpMethod.update:
            return AdminSerializer
        return UserSerializer

    def get_permissions(self):
        if self.request.method == HttpMethod.get:
            self.permission_classes = (IsAdminUser,)
        else:
            self.permission_classes = (UserAdminPermission,)
        return super(UserViewSet, self).get_permissions()
