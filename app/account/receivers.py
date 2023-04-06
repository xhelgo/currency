from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

import re

User = get_user_model()


@receiver(pre_save, sender=User)
def email_formatting_pre_save(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def phone_formatting_pre_save(sender, instance, **kwargs):
    if instance.phone:
        instance.phone = re.sub(r"[^0-9]", '', instance.phone)
