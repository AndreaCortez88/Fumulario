# Generated by Django 2.0.6 on 2021-09-30 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0004_auto_20210929_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='pesomascota',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='raza',
        ),
    ]
