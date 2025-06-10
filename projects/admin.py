from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "is_featured", "created_at"]
    list_filter = ["is_featured", "created_at"]
    search_fields = ["title", "description", "technologies"]
    fields = ["title", "description", "image", "github_url", "demo_url", "technologies", "is_featured"]