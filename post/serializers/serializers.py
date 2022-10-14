from rest_framework.fields import HiddenField
from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('uuid', 'page', 'content')
