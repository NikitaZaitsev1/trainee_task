from rest_framework.serializers import ModelSerializer

from page.models import Page


class PageSerializerUpdate(ModelSerializer):
    class Meta:
        model = Page
        fields = ('uuid', 'name', 'description', 'tags', 'image', 'is_private')
