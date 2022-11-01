from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import Method, Role
from page.models import Page, Tag
from page.permissions.page_user_permission import PageUserPermission
from page.serializers.page_serializer_moderator import PageModeratorSerializer
from page.serializers.page_serializer import PageSerializer
from page.serializers.page_serializer_update import PageSerializerUpdate
from page.serializers.tag_serializer import TagSerializer
from user.models import User


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()

    @action(methods=['get'], detail=True)
    def tags(self, request, pk=None):
        tags = Tag.objects.get(pk=pk)
        return Response({'tags': tags.name})

    @action(methods=['get'], detail=True)
    def users(self, request, pk=None):
        users = User.objects.get(pk=pk)
        return Response({'users': users.title})

    def get_serializer_class(self):
        if self.request.user.role == Role.USER and self.action == Method.UPDATE or self.action == Method.PARTIAL_UPDATE:
            return PageSerializerUpdate
        if self.request.user.role == Role.MODERATOR and self.action == Method.UPDATE or self.action == Method.PARTIAL_UPDATE:
            return PageModeratorSerializer
        return PageSerializer

    def get_permissions(self):
        if self.request.method == Method.GET:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (PageUserPermission,)
        return super(PageViewSet, self).get_permissions()


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
