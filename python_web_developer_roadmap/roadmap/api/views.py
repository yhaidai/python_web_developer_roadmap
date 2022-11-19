from rest_framework import viewsets

from ..models import RoadmapItem
from .serializers import RoadmapItemSerializer


class RoadmapItemViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = RoadmapItem.objects.all()
    serializer_class = RoadmapItemSerializer
