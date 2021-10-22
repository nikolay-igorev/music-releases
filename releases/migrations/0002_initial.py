# Generated by Django 3.2.8 on 2021-10-22 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('releases', '0001_initial'),
        ('labels', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasewholesaleprice',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wholesale_prices_for_currency', to='users.profilecurrency'),
        ),
        migrations.AddField(
            model_name='releasewholesaleprice',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wholesale_prices', to='releases.release'),
        ),
        migrations.AddField(
            model_name='releasewholesaleinfo',
            name='release',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='releases.release'),
        ),
        migrations.AddField(
            model_name='releasetradesinfo',
            name='release',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='releases.release'),
        ),
        migrations.AddField(
            model_name='release',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='labels.label'),
        ),
        migrations.AddField(
            model_name='release',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='release', to='users.profile'),
        ),
        migrations.AddField(
            model_name='marketinginfos',
            name='release',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='releases.release'),
        ),
        migrations.AddConstraint(
            model_name='releasewholesaleprice',
            constraint=models.UniqueConstraint(fields=('release', 'currency'), name='unique_price_per_release_and_currency'),
        ),
    ]
