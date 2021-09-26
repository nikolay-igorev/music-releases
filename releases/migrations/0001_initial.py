# Generated by Django 3.2.7 on 2021-09-26 04:47

import configuration.file_storage
import django.core.validators
from django.db import migrations, models
import django_countries.fields
import releases.models.release


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(blank=True, help_text='“Marketing” style of the release, i.e. instead of Black Metal -> Ethnic Black Metal from Sri Lanka', max_length=250, null=True)),
                ('release_overview', models.TextField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, help_text='Link to video teaser or complete track from the release', null=True, verbose_name='YouTube URL')),
                ('soundcloud_url', models.URLField(blank=True, help_text='Link to audio teaser or complete track from the release', null=True, verbose_name='SoundCloud URL')),
                ('press_feedback', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(help_text='Enter band name here. If split release - add band names with“/“ i.e. Nokturnal Mortum / Drudkh', max_length=250, verbose_name='Band name(s)')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Band country')),
                ('album_title', models.CharField(max_length=250, verbose_name='Album title')),
                ('release_date', models.DateField(blank=True, help_text='For past/old releases exact date is not important, feel free just to select January 1st, but with correct year. For recent/upcoming releases - please try to set the date exactly. This release will be shown in Upcoming Releases section.', null=True, verbose_name='Release date')),
                ('submitted_at', models.DateTimeField(blank=True, null=True, verbose_name='submitted date')),
                ('base_style', models.CharField(blank=True, choices=[('black_metal', 'Black Metal'), ('death_metal', 'Death Metal'), ('trash_metal', 'Thrash Metal')], max_length=250, null=True)),
                ('cover_image', models.ImageField(blank=True, help_text='Select image with minimum size of 800x800 pixel', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='images/covers/', verbose_name='Front cover image')),
                ('format', models.CharField(blank=True, choices=[('CD', 'CD'), ('Vinyl', 'Vinyl'), ('Tape', 'Tape'), ('DVD', 'DVD')], default='CD', max_length=5, null=True)),
                ('sample', models.FileField(blank=True, help_text='Upload up to 1 minute sample of the album to give fellow label owners a taste of this release', null=True, storage=configuration.file_storage.DuplicationFixFileSystemStorage(), upload_to='audios/releases/', validators=[releases.models.release.validate_file_size, django.core.validators.FileExtensionValidator(['mp3'])])),
                ('media_format_details', models.CharField(blank=True, help_text='E.g. Digipak, 2xGatefold etc.', max_length=250, null=True)),
                ('limited_edition', models.PositiveIntegerField(blank=True, null=True)),
                ('is_submitted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseTradesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_for_trade', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('trade_points', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseWholesaleInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_for_wholesale', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseWholesalePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
