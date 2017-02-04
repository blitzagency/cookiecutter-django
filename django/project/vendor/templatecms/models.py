from django.db import models
from django.contrib.postgres.fields import JSONField


class Copy(models.Model):
    copy = JSONField(blank=True, null=True)
