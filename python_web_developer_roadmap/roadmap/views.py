from django.shortcuts import render
from django.views.decorators.http import require_safe

from python_web_developer_roadmap.roadmap.api.views import RoadmapItemViewSet
from python_web_developer_roadmap.users.models import User


@require_safe
def personal_roadmap_view(request):
    name_contains = request.GET.get("name_contains")
    if name_contains is None:
        personal_roadmap_items = RoadmapItemViewSet.queryset.filter(author=request.user.id)
    else:
        personal_roadmap_items = RoadmapItemViewSet.queryset.filter(
            author=request.user.id, name__icontains=name_contains,
        )

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
