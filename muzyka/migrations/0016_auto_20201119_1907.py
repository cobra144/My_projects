# Generated by Django 3.1.1 on 2020-11-19 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0015_auto_20201119_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='zespoly',
            name='latitud',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zespoly',
            name='longitud',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
