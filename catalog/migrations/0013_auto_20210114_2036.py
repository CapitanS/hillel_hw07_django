# Generated by Django 3.1.4 on 2021-01-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_logmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]