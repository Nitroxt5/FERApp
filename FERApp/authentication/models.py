from django.db import models
from django.contrib.auth.models import User as DjangoUser


class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    uploads_count = models.PositiveIntegerField(default=0)
