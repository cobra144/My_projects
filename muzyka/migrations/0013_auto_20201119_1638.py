# Generated by Django 3.1.1 on 2020-11-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0012_uploadedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]