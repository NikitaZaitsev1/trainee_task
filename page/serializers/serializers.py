from rest_framework.serializers import ModelSerializer

from page.models import Page, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ('uuid', 'name', 'description', 'tags', 'owner', 'image')
