from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'email', 'image_s3_path', 'role', 'title', 'password')
