# Generated by Django 4.1.2 on 2022-10-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_rename_images_properties_image_properties_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='size',
            field=models.CharField(default=False, max_length=255),
            preserve_default=False,
        ),
    ]
