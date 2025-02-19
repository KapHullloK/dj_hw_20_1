from django.db import models

from dj_hw_20_1.settings import MEDIA_ROOT

NULLABLE = {"blank": True,
            "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    description = models.TextField(verbose_name="description", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(upload_to="images/", verbose_name="image", **NULLABLE)
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="price")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="creation date")
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name="last modified date")

    def __str__(self):
        return f"{self.name} {self.last_modified_date}"
