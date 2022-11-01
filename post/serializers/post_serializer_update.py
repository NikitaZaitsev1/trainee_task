from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializerUpdate(ModelSerializer):
    class Meta:
        model = Post
        fields = ('page', 'content')
