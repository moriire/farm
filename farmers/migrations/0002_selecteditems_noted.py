# Generated by Django 5.0 on 2023-12-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecteditems',
            name='noted',
            field=models.BooleanField(default=False),
        ),
    ]
