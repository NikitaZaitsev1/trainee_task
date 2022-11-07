from rest_framework.serializers import ModelSerializer

from post.models import Like


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('uuid', 'post', 'like_user', 'value')
