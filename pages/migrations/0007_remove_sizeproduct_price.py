# Generated by Django 4.1.4 on 2022-12-14 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_sizeproduct_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sizeproduct',
            name='price',
        ),
    ]