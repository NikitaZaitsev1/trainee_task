import os
import boto3
from django.core.mail import send_mail
from innotter import settings


class AwsService:

    @staticmethod
    def upload_to_s3(image, folder: str) -> bool:
        """Service for uploading a file to an S3 bucket"""

        # File to upload: image
        # Bucket to upload to: settings.AWS_STORAGE_BUCKET_NAME
        # S3 object name: f"/{folder}/{image.name}"

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

    @staticmethod
    def notify_by_mail(user_mails: list) -> int:  # user_mails: emails of followers
        """Service for sending emails to followers via AWS SES about publishing of new post"""
        subject = 'New post notification'
        message = 'We notify you that a new post was published'
        send_mail(
            subject,
            message,
            os.getenv("ADMIN_EMAIL"),
            user_mails,
            fail_silently=False,
        )
