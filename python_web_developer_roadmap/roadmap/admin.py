from django.contrib import admin  # noqa: F401

from python_web_developer_roadmap.roadmap.models import RoadmapItem


@admin.register(RoadmapItem)
class RoadmapItemAdmin(admin.ModelAdmin):
    pass
