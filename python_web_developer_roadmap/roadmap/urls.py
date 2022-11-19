from django.urls import path

from .views import roadmap_view

app_name = "roadmap"
urlpatterns = [
    path("", view=roadmap_view, name="roadmap_view"),
]
