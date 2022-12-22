from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from python_web_developer_roadmap.roadmap.api.views import RoadmapItemViewSet
from python_web_developer_roadmap.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("roadmap", RoadmapItemViewSet, basename='roadmap-item')


app_name = "api"
urlpatterns = router.urls
