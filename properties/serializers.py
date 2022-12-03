from rest_framework import serializers
from .models import Property, PropertyImages

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model: PropertyImages
        fields = ('id','property', 'image',)

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True
    )
    class Meta:
        model = Property
        fields = ('id','name', 'price', 'image', 'description','location','size', 'isFeatured','images', 'uploaded_images','created', 'updated')

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        property = Property.objects.create(**validated_data)
        for image in uploaded_images:
            newproperty_image = PropertyImages.objects.create(property=property, image=image)
        return property

