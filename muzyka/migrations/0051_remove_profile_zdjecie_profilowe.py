# Generated by Django 3.1.1 on 2021-04-07 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muzyka', '0050_profile_zdjecie_profilowe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='zdjecie_profilowe',
        ),
    ]
