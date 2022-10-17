from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from page.models import Page, Tag
from page.serializers.serializers import PageSerializer, TagSerializer
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


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
