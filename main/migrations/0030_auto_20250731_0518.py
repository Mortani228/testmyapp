# Generated by Django 3.1 on 2025-07-31 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20250731_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='modifications',
        ),
        migrations.AlterField(
            model_name='productmodification',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modifications', to='main.product'),
        ),
    ]
