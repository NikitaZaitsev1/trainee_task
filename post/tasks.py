from innotter.aws_service import AwsService
from innotter.celery import app


@app.task
def send_notification_email(user_email: str):
    AwsService().notify_by_mail(user_email)
