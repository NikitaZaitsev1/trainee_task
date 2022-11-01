from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import Method, Role
from user.models import User
from user.permissions.user_admin_permission import UserAdminPermission
from user.serializers.user_serializer_admin import UserSerializerAdmin
from user.serializers.user_serializer import UserSerializer
from user.serializers.user_serializer_get import UserSerializerGet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    lookup_field = 'title'

    def get_serializer_class(self):
        if self.action == Method.RETRIEVE or self.action == Method.LIST:
            return UserSerializerGet
        if self.request.user.role == Role.ADMIN and self.action == Method.UPDATE or self.action == Method.PARTIAL_UPDATE:
            return UserSerializerAdmin
        return UserSerializer

    def get_permissions(self):
        if self.request.method == Method.GET:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (UserAdminPermission,)
        return super(UserViewSet, self).get_permissions()
