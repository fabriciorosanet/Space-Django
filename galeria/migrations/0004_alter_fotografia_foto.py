# Generated by Django 4.2.16 on 2024-11-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_data_fotografia_fotografia_publicada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/'),
        ),
    ]
