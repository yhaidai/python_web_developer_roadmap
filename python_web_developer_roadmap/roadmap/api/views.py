from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from .pagination import StandardPageNumberPagination
from .permissions import IsAuthorOrReadOnly
from ..models import RoadmapItem
from .serializers import RoadmapItemSerializer


class RoadmapItemViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = RoadmapItem.objects.all()
    serializer_class = RoadmapItemSerializer
    pagination_class = StandardPageNumberPagination
    permission_classes = (IsAuthorOrReadOnly, )
    throttle_classes = (UserRateThrottle, )
    # Disable "PUT" method
    http_method_names = [m for m in viewsets.ModelViewSet.http_method_names if m not in ["put"]]

    @action(detail=True, url_path="description")
    def get_description(self, request: Request, uuid: str = None) -> Response:
        """
        Retrieve the contents of the roadmap item's file.

        Have to use different method name from `description`, not to override existing class attr.
        """
        roadmap_item = self.get_object()
        with roadmap_item.file.open() as description_file:
            return Response({"description": description_file.read()})
