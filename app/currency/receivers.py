from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from currency import constants
from currency.models import Rate


@receiver(post_save, sender=Rate)
def rate_create_clear_cache(sender, instance, created, **kwargs):
    if created:
        print('rate create cache clear')
        cache.delete(constants.LATEST_RATE_CACHE)
