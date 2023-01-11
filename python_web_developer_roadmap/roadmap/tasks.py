import os
from glob import glob

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

from python_web_developer_roadmap.roadmap.models import RoadmapItem

logger = get_task_logger(__name__)


@shared_task
def orphaned_files_cleanup():
    """
    This task is used to periodically cleanup orphaned files, which no longer have a roadmap item associated with them.
    """
    all_description_filepaths = set(glob(f"{settings.MEDIA_ROOT}/**/*.md", recursive=True))
    referenced_description_filepaths = set(
        os.path.join(settings.MEDIA_ROOT, roadmap_item.file.name)
        for roadmap_item in RoadmapItem.objects.all()
    )
    orphaned_description_filepaths = all_description_filepaths - referenced_description_filepaths
    for filepath in orphaned_description_filepaths:
        os.remove(filepath)
