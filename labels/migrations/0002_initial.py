# Generated by Django 3.2.8 on 2021-10-22 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to='users.profile'),
        ),
        migrations.AddConstraint(
            model_name='label',
            constraint=models.UniqueConstraint(fields=('name', 'profile'), name='unique_label_per_profile'),
        ),
        migrations.AddConstraint(
            model_name='label',
            constraint=models.UniqueConstraint(condition=models.Q(('is_main', True)), fields=('profile',), name='unique_main_label_per_profile'),
        ),
    ]
