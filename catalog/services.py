from django.conf import settings
from django.core.cache import cache

from catalog.models import Version, Category


def get_cached_version_for_product(product_pk):
    if settings.CACHE_ENABLED:
        key = f'version_list_{product_pk}'
        version_list = cache.get(key)
        if not version_list:
            version_list = Version.objects.filter(product__pk=product_pk)
            cache.set(key, version_list)
    else:
        version_list = Version.objects.filter(product__pk=product_pk)
    return version_list


def get_categories_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if not category_list:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list
