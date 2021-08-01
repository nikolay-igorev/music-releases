# Generated by Django 3.2.5 on 2021-08-01 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0007_rename_release_date_release_submitted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_date',
            field=models.DateField(default=datetime.date(2021, 8, 1), help_text='For past/old releases exact date is not important, feel free just to select January 1st, but with correct year. For recent/upcoming releases - please try to set the date exactly. This release will be shown in Upcoming Releases section.', verbose_name='Release date'),
        ),
        migrations.AlterField(
            model_name='release',
            name='submitted_at',
            field=models.DateField(blank=True, null=True, verbose_name='submitted date'),
        ),
    ]
