# Generated by Django 5.1.1 on 2024-09-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_productmodel_expiration'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='has_media',
            field=models.BooleanField(default=False),
        ),
    ]
