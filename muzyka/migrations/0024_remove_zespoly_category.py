# Generated by Django 3.1.1 on 2020-11-22 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0023_zespoly_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zespoly',
            name='category',
        ),
    ]