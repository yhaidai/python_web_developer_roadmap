from django.urls import path

from .views import personal_roadmap_view, official_roadmap_view

app_name = "roadmap"
urlpatterns = [
    path("personal/", view=personal_roadmap_view, name="personal_roadmap_view"),
    path("official/", view=official_roadmap_view, name="official_roadmap_view"),
]
