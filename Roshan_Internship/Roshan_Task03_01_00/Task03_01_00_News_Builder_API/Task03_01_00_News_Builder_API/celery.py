import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Task03_01_00_News_Builder_API.settings")

app = Celery("Task03_01_00_News_Builder_API")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

