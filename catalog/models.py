from django.db import models

from users.models import User

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="owner")
    is_published = models.BooleanField(default=False, verbose_name="is published")

    class Meta:
        permissions = [
            ("change_product_is_published", "Может менять статус публикации продукта"),
            ("change_product_description", "Может менять описание продукта"),
            ("change_product_category", "Может менять категорию продукта"),
        ]

    def __str__(self):
        return f"{self.name} {self.last_modified_date}"


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="number")
    name = models.CharField(max_length=100, verbose_name="name")
    active = models.BooleanField(default=True, verbose_name="active")
