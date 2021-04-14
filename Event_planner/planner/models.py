from django.contrib.auth.models import User
from django.db import models


class ResourceList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class EmailList(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class ThemeList(models.Model):
    event_type = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, unique=True)
    images = models.URLField(max_length=200)

    def __str__(self):
        return str(self.event_type)