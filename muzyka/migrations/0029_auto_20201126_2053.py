# Generated by Django 3.1.1 on 2020-11-26 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0028_auto_20201122_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zespoly',
            name='kategoria',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]