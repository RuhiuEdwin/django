# Generated by Django 3.2.3 on 2022-12-02 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_alter_propertyimages_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Properties',
            new_name='Property',
        ),
    ]
