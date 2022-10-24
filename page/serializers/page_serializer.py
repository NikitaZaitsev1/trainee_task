from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from innotter import settings
from page.models import Page
from services.upload_to_s3 import upload_to_s3


class PageSerializer(ModelSerializer):
    image = ImageField(required=False)

    class Meta:
        model = Page
        fields = ('uuid', 'name', 'description', 'tags', 'owner', 'followers', 'image')

    def create(self, validated_data):
        page = Page.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=validated_data['owner']
        )

        image = validated_data.get('image')
        if image is not None:
            upload_to_s3(image, folder="page")
            page.image_s3_path = f"{settings.DEFAULT_AWS_STORAGE_URL}/page/{image.name}"

        page.save()
        return page
