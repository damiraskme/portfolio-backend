from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  technologies_list = serializers.SerializerMethodField()
  image_url = serializers.SerializerMethodField()

  class Meta:
    model = Project
    fields = [
      "id", "title", "description", "image", "image_url",
      "github_url", "demo_url", "technologies", "technologies_list",
      "is_featured", "created_at", "updated_at"
    ]
    read_only_fields = ["id", "created_at", "updated_at"]

  def get_technologies_list(self, obj):
    return obj.get_technologies_list()

  def get_image_url(self, obj):
    request = self.context.get("request")
    if obj.image and hasattr(obj.image, "url"):
      if request:
        return request.build_absolute_uri(obj.image.url)
      return obj.image.url
    return None

  def validate_title(self, value):
    if not value.strip():
      raise serializers.ValidationError("Title cannot be empty.")
    return value.strip()

  def validate_description(self, value):
    if not value.strip():
      raise serializers.ValidationError("Description cannot be empty.")
    return value.strip()