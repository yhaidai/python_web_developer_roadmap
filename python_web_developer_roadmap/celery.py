from celery import Celery

app = Celery("python_web_developer_roadmap")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
