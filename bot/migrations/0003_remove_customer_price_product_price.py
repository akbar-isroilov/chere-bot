# Generated by Django 5.0.6 on 2024-06-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_customer_is_company_customer_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
