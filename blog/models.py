from django.db import models

NULLABLE = {"blank": True,
            "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    slug = models.CharField(unique=True, max_length=100, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name="content", **NULLABLE)
    img = models.ImageField(upload_to="images/", verbose_name="image", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    is_published = models.BooleanField(default=False, verbose_name="is published")
    views = models.IntegerField(default=0, verbose_name="views")

    def __str__(self):
        return f"{self.title}"
