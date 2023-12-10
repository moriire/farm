# Generated by Django 5.0 on 2023-12-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.CharField(choices=[('BAG', 'Bag'), ('FARM', 'Farm'), ('BASKET', 'Basket')], max_length=20, null=True)),
                ('measure', models.CharField(max_length=20, null=True)),
                ('desc', models.TextField(default='')),
            ],
        ),
    ]
