# Generated by Django 5.1.1 on 2024-10-02 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_alter_scheduling_description'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sales_intern',
        ),
        migrations.AlterField(
            model_name='scheduling',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.order'),
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='available',
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
