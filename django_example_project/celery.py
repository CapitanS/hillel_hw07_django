import os

from celery import Celery
from celery.schedules import crontab  # scheduler

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_example_project.settings')

app = Celery('django_example_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# scheduled task execution
app.conf.beat_schedule = {
    # executes every odd hour
    'scraping-task-odd-hour': {
        'task': 'scraping.tasks.scraping_quotes',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}
