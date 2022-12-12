from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    uploads_count = models.PositiveIntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  # NOQA
        if created:
            Profile.objects.create(user=instance)  # NOQA

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  # NOQA
        instance.profile.save()
