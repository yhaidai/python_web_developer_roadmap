from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "python_web_developer_roadmap.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import python_web_developer_roadmap.users.signals  # noqa F401
        except ImportError:
            pass
