from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'description', 'location', 'isFeatured', 'images', 'size', 'created', 'updated')

# Register your models here.

admin.site.register(Property, PropertyAdmin)