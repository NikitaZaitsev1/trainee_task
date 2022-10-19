from rest_framework.serializers import ModelSerializer

from page.models import Page


class PageSerializer(ModelSerializer):
    # owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Page
        fields = ('uuid', 'name', 'description', 'tags', 'owner', 'image')
