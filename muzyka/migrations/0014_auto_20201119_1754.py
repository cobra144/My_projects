# Generated by Django 3.1.1 on 2020-11-19 17:54

from django.db import migrations, models
import django.utils.timezone
import exiffield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0013_auto_20201119_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='zespoly',
            name='camera',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zespoly',
            name='exif',
            field=exiffield.fields.ExifField(default={}, editable=False),
        ),
    ]
