# Generated by Django 5.0.6 on 2024-06-29 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='default_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='default_products', to='shop.category'),
        ),
    ]
