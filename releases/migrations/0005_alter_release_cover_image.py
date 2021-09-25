# Generated by Django 3.2.7 on 2021-09-25 12:37

import configuration.file_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0004_alter_release_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='cover_image',
            field=models.ImageField(blank=True, help_text='Select image with minimum size of 800x800 pixel', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='images/covers/', verbose_name='Front cover image'),
        ),
    ]
