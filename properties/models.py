#menu/models.py
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()
    # images = models.FileField()
    isFeatured = models.BooleanField(default=False)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images", default='')
    image = models.ImageField(upload_to="media",default="", null=True, blank=True)