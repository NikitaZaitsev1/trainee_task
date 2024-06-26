from rest_framework.fields import CharField, ImageField
from rest_framework.serializers import ModelSerializer

from innotter import settings
from innotter.aws_service import AwsService
from user.models import User


class UserSerializer(ModelSerializer):
    password = CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    image_s3_path = ImageField(required=False)

    class Meta:
        model = User
        fields = ('uuid', 'username', 'email', 'image_s3_path', 'role', 'title', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'User'),
            title=validated_data['title'],
            password=validated_data['password'],

        )
        image = validated_data.get('image_s3_path')
        if image is not None:
            AwsService().upload_to_s3(image, folder="user")
            user.image_s3_path = f"{settings.DEFAULT_AWS_STORAGE_URL}/user/{image.name}"

        user.save()
        return user
