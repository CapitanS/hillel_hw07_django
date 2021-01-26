from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_with_reminder(text, email):
    send_mail(
        subject='Reminder',
        message=text,
        from_email='server@server.com',
        recipient_list=[email]
    )
