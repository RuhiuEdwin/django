# Generated by Django 3.2.3 on 2022-12-03 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_alter_property_isfeatured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='isFeatured',
        ),
    ]
