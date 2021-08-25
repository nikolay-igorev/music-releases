# Generated by Django 3.2.6 on 2021-08-25 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('band_submission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandsubmission',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='users.profile'),
        ),
    ]
