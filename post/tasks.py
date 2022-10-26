from innotter.celery import app
from innotter.email_service import EmailService


@app.task
def send_notification_email(user_emails: list):
    """Celery task for sending emails to followers via AWS SES about publishing of new post"""
    EmailService().notify_by_mail(user_emails)
