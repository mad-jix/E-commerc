# Generated by Django 5.0.2 on 2024-07-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_cart_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='orederstatus',
            field=models.IntegerField(choices=[(1, 'ORDER_PROCESSED'), (2, 'DELIVERED'), (3, 'REJECTED')], default=0),
        ),
    ]
