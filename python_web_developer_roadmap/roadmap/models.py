import uuid
from os import PathLike

from django.db import models

from python_web_developer_roadmap.users.models import User


def get_upload_path(instance: "RoadmapItem", filename: PathLike) -> str:
    """
    Used instead of a seemingly neater lambda, due to https://stackoverflow.com/a/27074816
    """
    return f"roadmap_items/{instance.author.username}/{instance.name}_{instance.uuid}.md"


class RoadmapItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to=get_upload_path)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        "RoadmapItem", on_delete=models.CASCADE, null=True, blank=True,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return f"Roadmap Item: {self.name}"

    def __repr__(self) -> str:
        return (f"RoadmapItem(author={self.author}, name={self.name}, file={self.file}, "
                f"parent={self.parent}, uuid={self.uuid})")
