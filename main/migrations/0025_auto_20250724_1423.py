# Generated by Django 3.1 on 2025-07-24 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_productmodification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storageitem',
            old_name='description',
            new_name='modification',
        ),
    ]
