# Generated by Django 5.0.1 on 2024-01-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restasite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
