# Generated by Django 3.1.1 on 2020-11-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0005_auto_20201118_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='zespoly',
            name='meta',
            field=models.TextField(default=''),
        ),
    ]
