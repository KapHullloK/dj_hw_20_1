from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            {"name": "var1", "description": "s sd"},
            {"name": "var2", "description": "gf a"},
        ]

        for cat in categories:
            Category.objects.create(**cat)

        products = [
            {"name": "viks", "description": "cvx",
             "category": Category.objects.get(name="var1"), "price": 150.5},
            {"name": "gids", "description": "asd a",
             "category": Category.objects.get(name="var2"), "price": 80.9},
        ]

        for prod in products:
            Product.objects.create(**prod)
