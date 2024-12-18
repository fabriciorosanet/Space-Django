# Generated by Django 4.2.16 on 2024-11-26 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='legenda',
            field=models.CharField(max_length=150),
        ),
    ]
