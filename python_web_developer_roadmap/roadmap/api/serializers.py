import io
from typing import Any

from django.contrib.auth import get_user_model
from django.core.files import File
from rest_framework import serializers

from ..models import RoadmapItem


class RoadmapItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for `RoadmapItem` model.
    """

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
    #: Comes as a text from frontend, is written to a file during deserialization
    description = serializers.CharField(max_length=10_000, default="", allow_blank=True, write_only=True)
    #: For demo purposes
    file_relative_path = serializers.SerializerMethodField("get_file_relative_path")

    class Meta:
        model = RoadmapItem
        fields = ("author", "name", "description", "parent", "uuid", "file_relative_path")

    def get_file_relative_path(self, roadmap_item: RoadmapItem) -> str:
        """
        For demo purposes.
        """
        return roadmap_item.file.name

    def create(self, validated_data: dict[str, Any]):
        file = io.StringIO(validated_data.pop("description"))
        validated_data["file"] = File(file=file, name="placeholder")
        return super().create(validated_data)

    def update(self, roadmap_item: RoadmapItem, validated_data: dict[str, Any]):
        roadmap_item.name = validated_data.get("name", roadmap_item.name)
        roadmap_item.author = validated_data.get("author", roadmap_item.author)
        roadmap_item.parent = validated_data.get("parent", roadmap_item.parent)

        with roadmap_item.file.open("w") as description_file:
            # "description" is required
            description_file.write(validated_data["description"])

        roadmap_item.save()
        return roadmap_item
