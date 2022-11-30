#menu/models.py
from django.db import models

class Properties(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    # images = models.FileField()
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MultipleImage(models.Model):
    images = models.FileField()