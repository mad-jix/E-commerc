# Generated by Django 5.0.2 on 2024-06-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='oreder_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROCESSED'), (3, 'DELIVERED'), (4, 'REJECTED')], default=0),
        ),
    ]