# Generated by Django 3.0.5 on 2020-04-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
