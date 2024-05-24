from django.db import models
from django.utils import timezone


class NameMixin(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    description = models.TextField(default='', blank=True)

    class Meta:
        abstract = True


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DateTimesABC(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IsDraftMixin(models.Model):
    is_draft = models.BooleanField(default=False)

    class Meta:
        abstract = True
