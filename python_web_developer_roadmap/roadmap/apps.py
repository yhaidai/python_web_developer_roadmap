from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RoadmapConfig(AppConfig):
    name = "python_web_developer_roadmap.roadmap"
    verbose_name = _("Roadmap")
