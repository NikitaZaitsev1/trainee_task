from rest_framework.serializers import ModelSerializer

from page.models import Page


class PageModeratorSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ('uuid', 'description', 'is_blocked')
