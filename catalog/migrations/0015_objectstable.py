# Generated by Django 3.1.4 on 2021-01-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_utilizationrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('object_info', models.JSONField(db_column='Information')),
                ('customer', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
