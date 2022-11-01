from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializerGet(ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'email', 'title', 'is_blocked')
