from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
  path("profile/", views.ProfileDetailView.as_view(), name="profile-detail"),
  path("profile/summary/", views.profile_summary, name="profile-summary"),
]