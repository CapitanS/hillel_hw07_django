# Generated by Django 3.1.4 on 2021-01-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(to='orders.Product', verbose_name='products of customer'),
        ),
    ]
