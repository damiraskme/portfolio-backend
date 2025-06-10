from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer
  
  def get_object(self):
    profile, created = Profile.objects.get_or_create(
      pk=1,
      defaults={
        "email": "your-email@example.com",
        "github_url": "",
        "linkedin_url": "",
        "bio": ""
      }
    )
    return profile

@api_view(["GET"])
def profile_summary(request):
  try:
    profile = Profile.objects.first()
    if profile:
      data = {
        "email": profile.email,
        "github_url": profile.github_url,
        "linkedin_url": profile.linkedin_url,
      }
      return Response(data)
    else:
      return Response({
        "email": "",
        "github_url": "",
        "linkedin_url": "",
      })
  except Exception as e:
    return Response(
      {"error": "Failed to fetch profile"}, 
      status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )