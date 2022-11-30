from django.contrib import admin
from .models import Properties

class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'description', 'location', 'size', 'created', 'updated')

# Register your models here.

admin.site.register(Properties, PropertiesAdmin)