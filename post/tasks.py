from innotter.aws_service import AwsService
from innotter.celery import app


@app.task
def send_notification_email(user_emails: list):
    """Celery task for sending emails to followers via AWS SES about publishing of new post"""
    AwsService().notify_by_mail(user_emails)
