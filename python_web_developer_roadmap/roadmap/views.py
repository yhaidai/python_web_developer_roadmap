from django.shortcuts import render
from django.urls import reverse

from python_web_developer_roadmap.roadmap.utils import get_request


def roadmap_view(request):
    roadmap_api_url = request.build_absolute_uri(reverse("api:roadmapitem-list"))
    roadmap_api_response = get_request(request, roadmap_api_url)
    roadmap_items = roadmap_api_response.json()

    return render(
        request,
        "roadmap/base.html",
        context={
            "roadmap_items": roadmap_items,
        },
    )
