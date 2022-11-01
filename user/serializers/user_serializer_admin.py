from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializerAdmin(ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'role', 'is_blocked')
