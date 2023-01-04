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

    def get_file_relative_path(self, obj):
        """
        For demo purposes.
        """
        return obj.file.name

    def create(self, validated_data: dict[str, Any]):
        """
        Deserialize for a POST request.

        Description field is written to a file and dropped.
        """
        file = io.StringIO(validated_data.pop("description"))

        # Create roadmap item, so that we can use its UUID in the filename
        validated_data["file"] = File(file=file, name="placeholder")
        return super().create(validated_data)
