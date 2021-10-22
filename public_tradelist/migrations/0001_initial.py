# Generated by Django 3.2.8 on 2021-10-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradeRequestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=250, verbose_name='Band name(s)')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('trade_points', models.DecimalField(decimal_places=1, max_digits=3)),
                ('prices_with_currencies', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
