# Generated by Django 3.1.1 on 2020-11-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0003_auto_20201118_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zespoly',
            name='camera',
            field=models.TextField(default='', editable=False, max_length=100),
        ),
    ]
