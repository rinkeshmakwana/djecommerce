# Generated by Django 3.0.5 on 2020-04-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_order_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=20),
            preserve_default=False,
        ),
    ]
