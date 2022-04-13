# Generated by Django 4.0.1 on 2022-04-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_customer_address_customer_city_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerAddress',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos'),
        ),
    ]
