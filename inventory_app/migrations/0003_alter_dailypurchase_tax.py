# Generated by Django 5.0.7 on 2024-08-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_dailypurchase_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailypurchase',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]