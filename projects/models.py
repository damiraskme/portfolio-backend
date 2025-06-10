from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to="projects/", blank=True, null=True)
  github_url = models.URLField(max_length=200, blank=True)
  demo_url = models.URLField(max_length=200, blank=True)
  technologies = models.CharField(max_length=300, help_text="Comma-separated list of technologies")
  is_featured = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ["-created_at"]

  def __str__(self):
    return self.title

  def get_technologies_list(self):
    return [tech.strip() for tech in self.technologies.split(",") if tech.strip()]
