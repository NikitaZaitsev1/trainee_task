from rest_framework.serializers import ModelSerializer

from post.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('uuid', 'post', 'reply_to', 'text', 'date_added')
