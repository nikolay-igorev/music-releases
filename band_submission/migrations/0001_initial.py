# Generated by Django 3.2.6 on 2021-08-25 07:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('demo_sample', models.FileField(upload_to='band_submissions/audio/', validators=[django.core.validators.FileExtensionValidator(['mp3', 'zip', 'rar'])])),
                ('front_cover', models.ImageField(blank=True, null=True, upload_to='band_submissions/image/', verbose_name='front cover')),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField(help_text='Write about releases, press mention or tour dates')),
            ],
        ),
    ]
