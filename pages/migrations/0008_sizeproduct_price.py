# Generated by Django 4.1.4 on 2022-12-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_sizeproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizeproduct',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
