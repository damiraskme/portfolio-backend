from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at", "updated_at"]
    fields = ["email", "github_url", "linkedin_url", "bio"]