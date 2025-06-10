from django.db import models

class Profile(models.Model):
  email = models.EmailField(max_length=254)
  github_url = models.URLField(max_length=200, blank=True)
  linkedin_url = models.URLField(max_length=200, blank=True)
  bio = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Profile - {self.email}"

  class Meta:
    verbose_name = "Profile"
    verbose_name_plural = "Profile"