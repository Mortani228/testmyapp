# Generated by Django 3.1 on 2025-07-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
