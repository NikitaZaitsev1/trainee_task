from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import HttpMethod, Role
from page.models import Page, Tag
from page.permissions.page_user_permission import PageUserPermission
from page.serializers.page_moderator_serializer import PageModeratorSerializer
from page.serializers.page_serializer import PageSerializer
from page.serializers.tag_serializer import TagSerializer
from user.models import User


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    @action(methods=['get'], detail=True)
    def tags(self, request, pk=None):
        tags = Tag.objects.get(pk=pk)
        return Response({'tags': tags.name})

    @action(methods=['get'], detail=True)
    def users(self, request, pk=None):
        users = User.objects.get(pk=pk)
        return Response({'users': users.title})

    def get_permissions(self):
        if self.request.method == HttpMethod.get:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (PageUserPermission,)
        return super(PageViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == HttpMethod.retrieve or self.action == HttpMethod.update and self.request.user == Role.moderator:
            return PageModeratorSerializer
        return PageSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
