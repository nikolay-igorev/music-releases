# Generated by Django 3.2.7 on 2021-09-30 12:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import releases.models.release


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('releases', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='cover_image',
            field=models.ImageField(help_text='Select image with minimum size of 800x800 pixel', upload_to='images/covers/', verbose_name='Front cover image'),
        ),
        migrations.AlterField(
            model_name='release',
            name='sample',
            field=models.FileField(help_text='Upload up to 1 minute sample of the album to give fellow label owners a taste of this release', upload_to='audios/releases/', validators=[releases.models.release.validate_file_size, django.core.validators.FileExtensionValidator(['mp3'])]),
        ),
        migrations.CreateModel(
            name='FavouriteRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_releases', to='users.profile')),
                ('release', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_object', to='releases.release')),
            ],
        ),
    ]
