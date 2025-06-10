from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ["id", "email", "github_url", "linkedin_url", "bio", "created_at", "updated_at"]
    read_only_fields = ["id", "created_at", "updated_at"]

  def validate_email(self, value):
    if not value:
      raise serializers.ValidationError("Email is required.")
    return value