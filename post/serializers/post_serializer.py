from rest_framework.serializers import ModelSerializer

from page.models import Page
from post.models import Post
from post.tasks import send_notification_email


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('uuid', 'page', 'content')

    def create(self, validated_data):
        post = Post.objects.create(
            page=validated_data['page'],
            content=validated_data['content'],
        )

        post.save()
        send_notification_email.delay(
            Page.get_emails(post.page.uuid))  # Sending emails to followers via AWS SES using Celery

        return post
