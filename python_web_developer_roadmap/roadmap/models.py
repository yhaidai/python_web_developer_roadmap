import uuid

from django.db import models

from python_web_developer_roadmap.users.models import User


class RoadmapItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "RoadmapItem", on_delete=models.CASCADE, null=True, blank=True
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
