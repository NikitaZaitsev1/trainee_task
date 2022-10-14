from rest_framework.viewsets import ModelViewSet

from page.models import Page, Tag
from page.serializers.serializers import PageSerializer, TagSerializer


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
