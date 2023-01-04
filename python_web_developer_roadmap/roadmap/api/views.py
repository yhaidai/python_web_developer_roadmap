from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from ..models import RoadmapItem
from .serializers import RoadmapItemSerializer


class RoadmapItemViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = RoadmapItem.objects.all()
    serializer_class = RoadmapItemSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    @action(detail=True, url_path="description")
    def get_description(self, request, uuid=None):
        """
        Retrieve the contents of the roadmap item's file.

        Have to use different method name from `description`, not to override existing class attr.
        """
        roadmap_item = self.get_object()
        with roadmap_item.file.open() as description_file:
            return Response({"description": description_file.read()})
