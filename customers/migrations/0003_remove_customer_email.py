# Generated by Django 5.0.2 on 2024-06-26 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
