# Generated by Django 5.0.2 on 2024-07-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_cart_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='city',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]