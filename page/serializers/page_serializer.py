from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from innotter import settings
from innotter.aws_service import AwsService
from page.models import Page


class PageSerializer(ModelSerializer):
    image = ImageField(required=False)

    class Meta:
        model = Page
        fields = ('uuid', 'name', 'description', 'tags', 'owner', 'followers', 'image', 'is_private')

    def create(self, validated_data):
        page = Page.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=validated_data['owner']
        )

        image = validated_data.get('image')
        if image is not None:
            AwsService().upload_to_s3(image, folder="page")
            page.image_s3_path = f"{settings.DEFAULT_AWS_STORAGE_URL}/page/{image.name}"

        page.save()
        return page
