# Generated by Django 4.1.4 on 2022-12-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0003_methods_tarif_remove_rate_type_delete_cargomethod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='methods',
            name='countryandmethod',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
