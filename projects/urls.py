from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
  path("projects/", views.ProjectListCreateView.as_view(), name="project-list-create"),
  path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail"),
  path("projects/count/", views.project_count, name="project-count"),
  path("projects/<int:pk>/toggle-featured/", views.toggle_featured, name="toggle-featured"),
]