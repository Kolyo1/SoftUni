import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vinyl_collection.settings')

app = Celery('vinyl_collection')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Schedule periodic tasks
app.conf.beat_schedule = {
    'generate-collection-statistics': {
        'task': 'records.tasks.generate_collection_statistics',
        'schedule': crontab(hour=0, minute=0),  # Daily at midnight
    },
    'cleanup-old-notifications': {
        'task': 'users.tasks.cleanup_old_notifications',
        'schedule': crontab(hour=2, minute=0, day_of_week=1),  # Weekly on Monday at 2 AM
    },
    'update-wishlist-availability': {
        'task': 'wishlist.tasks.update_wishlist_availability',
        'schedule': crontab(hour=6, minute=0),  # Daily at 6 AM
    },
}
