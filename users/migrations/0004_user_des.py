# Generated by Django 5.0 on 2023-12-15 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='des',
            field=models.CharField(choices=[('BUYER', 'Buyer'), ('FARMER', 'Farmer')], default='FARMER', max_length=10),
            preserve_default=False,
        ),
    ]
