# Generated by Django 3.1.1 on 2020-11-18 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0004_auto_20201118_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zespoly',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='zespoly',
            name='exif',
        ),
    ]