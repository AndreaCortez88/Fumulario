# Generated by Django 2.0.6 on 2021-09-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='peso',
            field=models.CharField(max_length=100),
        ),
    ]
