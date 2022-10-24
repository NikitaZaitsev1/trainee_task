import boto3

from innotter import settings

"""Service for uploading a file to an S3 bucket"""


# File to upload: image
# Bucket to upload to: settings.AWS_STORAGE_BUCKET_NAME
# S3 object name: f"/{folder}/{image.name}"


def upload_to_s3(image, folder: str) -> bool:
    client_s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    client_s3.upload_fileobj(
        image,
        settings.AWS_STORAGE_BUCKET_NAME,
        f"/{folder}/{image.name}"
    )
