from django.core.mail import send_mail
from django_example_project.celery import app


@app.task
def send_email_with_reminder(text, email):
    send_mail(
        subject='Reminder',
        message=text,
        from_email=email,
        fail_silently=False,
    )
