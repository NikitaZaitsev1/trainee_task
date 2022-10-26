import os

from django.core.mail import send_mail


class EmailService:
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
