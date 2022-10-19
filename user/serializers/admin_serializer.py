from rest_framework.serializers import ModelSerializer

from user.models import User


class AdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'is_blocked',)
