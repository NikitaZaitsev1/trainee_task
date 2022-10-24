from rest_framework.serializers import ModelSerializer

from post.models import Post
from post.tasks import send_notification_email
from user.models import User


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('uuid', 'page', 'content')

    def create(self, validated_data):
        post = Post.objects.create(
            page=validated_data['page'],
            content=validated_data['content'],
        )

        for follower in post.page.followers.all():
            for user in User.objects.all():
                if follower.uuid == user.uuid:
                    send_notification_email(user.email)
        post.save()
        return post
