# Generated by Django 3.1.1 on 2020-11-19 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0016_auto_20201119_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zespoly',
            old_name='latitud',
            new_name='Xres',
        ),
        migrations.RenameField(
            model_name='zespoly',
            old_name='longitud',
            new_name='Yres',
        ),
    ]
