# Generated by Django 5.0 on 2023-12-20 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_selecteditems_noted'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
