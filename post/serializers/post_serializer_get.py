from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializerGet(ModelSerializer):
    class Meta:
        model = Post
        fields = ('uuid', 'page', 'content', 'created_at', 'updated_at')
