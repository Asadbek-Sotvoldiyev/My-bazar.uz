# Generated by Django 5.0.2 on 2024-03-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_products_product_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]