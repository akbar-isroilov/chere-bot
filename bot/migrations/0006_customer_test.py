# Generated by Django 5.0.6 on 2024-06-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_customer_latitude_customer_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='test',
            field=models.URLField(default='https://google.com'),
            preserve_default=False,
        ),
    ]
