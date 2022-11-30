from rest_framework import serializers
from .models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ('id','name', 'price', 'image', 'description','location','size', 'created', 'updated')