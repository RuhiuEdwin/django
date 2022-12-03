# Generated by Django 3.2.3 on 2022-12-02 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_multipleimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.properties')),
            ],
        ),
        migrations.DeleteModel(
            name='MultipleImage',
        ),
    ]