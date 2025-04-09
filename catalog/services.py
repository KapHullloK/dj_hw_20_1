from django.core.cache import cache

from catalog.models import Category
from dj_hw_20_1 import settings


def get_categories():
    return Category.objects.all()


def get_categories_from_cache():
    key = 'categories'

    if settings.CACHE_ENABLED:
        cache_data = cache.get(key)

        if cache_data:
            return cache_data

    queryset = get_categories()
    cache.set(key, queryset)

    return queryset