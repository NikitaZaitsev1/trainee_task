from rest_framework.serializers import ModelSerializer

from page.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('uuid', 'name')
