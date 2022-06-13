from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(instance, created, *args, **kwargs):
    """Signal to auto-create a profile for newly created user"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_token(instance, created, *args, **kwargs):
    """Signal to create auth token for newly created user"""
    if created:
        Token.objects.create(user=instance)
