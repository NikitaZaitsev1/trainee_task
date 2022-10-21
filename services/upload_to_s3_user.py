import boto3

from innotter import settings


def upload_to_s3(image, folder: str):
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
