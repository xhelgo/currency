from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path
    )
    phone = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
