from django.shortcuts import render

from python_web_developer_roadmap.roadmap.api.views import RoadmapItemViewSet
from python_web_developer_roadmap.users.models import User


def personal_roadmap_view(request):
    personal_roadmap_items = RoadmapItemViewSet.queryset.filter(author=request.user.id)
    return render(
        request,
        "roadmap/personal_roadmap.html",
        context={
            "roadmap_items": personal_roadmap_items,
        },
    )


def official_roadmap_view(request):
    admin_users = User.objects.filter(is_staff=True)
    official_roadmap_items = RoadmapItemViewSet.queryset.filter(author__in=admin_users)
    return render(
        request,
        "roadmap/official_roadmap.html",
        context={
            "roadmap_items": official_roadmap_items,
        },
    )
