# Generated by Django 3.1.1 on 2020-11-18 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0007_auto_20201118_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zespoly',
            name='meta',
        ),
    ]