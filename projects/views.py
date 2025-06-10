from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

  def get_queryset(self):
    queryset = Project.objects.all()
    featured = self.request.query_params.get("featured", None)
    if featured and featured.lower() == "true":
      queryset = queryset.filter(is_featured=True)
    return queryset

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer

@api_view(["GET"])
def project_count(request):
  count = Project.objects.count()
  featured_count = Project.objects.filter(is_featured=True).count()
  
  return Response({
    "total_projects": count,
    "featured_projects": featured_count
  })

@api_view(["POST"])
def toggle_featured(request, pk):
  try:
    project = get_object_or_404(Project, pk=pk)
    project.is_featured = not project.is_featured
    project.save()
    
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)
  except Exception as e:
    return Response(
      {"error": "Failed to toggle featured status"}, 
      status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )