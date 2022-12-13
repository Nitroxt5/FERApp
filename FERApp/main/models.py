import os

from .validators import validate_file_size, no_space_title_validator

from django.db import models
from django.contrib.auth.models import User


def get_upload_to(instance, filename):
    return os.path.join(str(instance.user.id), filename)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=15, validators=[no_space_title_validator])
    image = models.ImageField(upload_to=get_upload_to, validators=[validate_file_size])
