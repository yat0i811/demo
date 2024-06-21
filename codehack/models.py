from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    text = models.TextField(blank=True, null=True)
    fields = models.JSONField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)