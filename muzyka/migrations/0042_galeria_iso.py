# Generated by Django 3.1.1 on 2020-12-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0041_auto_20201220_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='iso',
            field=models.CharField(default='1', editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
