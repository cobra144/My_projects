# Generated by Django 3.1.1 on 2020-11-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0021_auto_20201122_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zespoly',
            name='kategoria',
            field=models.CharField(max_length=32),
        ),
    ]
