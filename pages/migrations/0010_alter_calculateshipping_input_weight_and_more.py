# Generated by Django 4.1.4 on 2022-12-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_calculateshipping_delete_sizeproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculateshipping',
            name='input_weight',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='calculateshipping',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]