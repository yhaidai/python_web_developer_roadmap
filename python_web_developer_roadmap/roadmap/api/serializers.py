from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import RoadmapItem


class RoadmapItemSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        allow_null=True,
        queryset=get_user_model().objects.all(),
        slug_field="username",
    )
    parent = serializers.SlugRelatedField(
        allow_null=True,
        queryset=RoadmapItem.objects.all(),
        slug_field="uuid",
    )

    class Meta:
        model = RoadmapItem
        fields = ("author", "description", "name", "parent", "uuid")
