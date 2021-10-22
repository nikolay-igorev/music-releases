# Generated by Django 3.2.8 on 2021-10-22 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import users.models.user_manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('releases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(help_text='Full name/alias/nickname as you would usually sign your emails, e.g. John Johnson or Lord Demogorgon.', max_length=255, verbose_name='Name')),
                ('email', models.EmailField(help_text='The email address of the main label. It will be needed for logging in.', max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.models.user_manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.TextField(blank=True, null=True)),
                ('submission_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('trade_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(related_name='wished_by_profiles', to='releases.Release')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD - US Dollar'), ('EUR', 'EUR - Euro'), ('AED', 'AED - UAE Dirham'), ('AFN', 'AFN - Afghani'), ('ALL', 'ALL - Lek'), ('AMD', 'AMD - Armenian Dram'), ('ANG', 'ANG - Netherlands Antillean Guilder'), ('AOA', 'AOA - Kwanza'), ('ARS', 'ARS - Argentine Peso'), ('AUD', 'AUD - Australian Dollar'), ('AWG', 'AWG - Aruban Florin'), ('AZN', 'AZN - Azerbaijanian Manat'), ('BAM', 'BAM - Convertible Mark'), ('BBD', 'BBD - Barbados Dollar'), ('BDT', 'BDT - Taka'), ('BGN', 'BGN - Bulgarian Lev'), ('BHD', 'BHD - Bahraini Dinar'), ('BIF', 'BIF - Burundi Franc'), ('BMD', 'BMD - Bermudian Dollar'), ('BND', 'BND - Brunei Dollar'), ('BOB', 'BOB - Boliviano'), ('BRL', 'BRL - Brazilian Real'), ('BSD', 'BSD - Bahamian Dollar'), ('BTN', 'BTN - Ngultrum'), ('BWP', 'BWP - Pula'), ('BYN', 'BYN - Belarusian Ruble'), ('BZD', 'BZD - Belize Dollar'), ('CAD', 'CAD - Canadian Dollar'), ('CDF', 'CDF - Congolese Franc'), ('CHF', 'CHF - Swiss Franc'), ('CLP', 'CLP - Chilean Peso'), ('CNY', 'CNY - Yuan Renminbi'), ('COP', 'COP - Colombian Peso'), ('CRC', 'CRC - Costa Rican Colon'), ('CUC', 'CUC - Peso Convertible'), ('CUP', 'CUP - Cuban Peso'), ('CVE', 'CVE - Cabo Verde Escudo'), ('CZK', 'CZK - Czech Koruna'), ('DJF', 'DJF - Djibouti Franc'), ('DKK', 'DKK - Danish Krone'), ('DOP', 'DOP - Dominican Peso'), ('DZD', 'DZD - Algerian Dinar'), ('EGP', 'EGP - Egyptian Pound'), ('ERN', 'ERN - Nakfa'), ('ETB', 'ETB - Ethiopian Birr'), ('FJD', 'FJD - Fiji Dollar'), ('FKP', 'FKP - Falkland Islands Pound'), ('GBP', 'GBP - Pound Sterling'), ('GEL', 'GEL - Lari'), ('GHS', 'GHS - Ghana Cedi'), ('GIP', 'GIP - Gibraltar Pound'), ('GMD', 'GMD - Dalasi'), ('GNF', 'GNF - Guinea Franc'), ('GTQ', 'GTQ - Quetzal'), ('GYD', 'GYD - Guyana Dollar'), ('HKD', 'HKD - Hong Kong Dollar'), ('HNL', 'HNL - Lempira'), ('HRK', 'HRK - Kuna'), ('HTG', 'HTG - Gourde'), ('HUF', 'HUF - Forint'), ('IDR', 'IDR - Rupiah'), ('ILS', 'ILS - New Israeli Sheqel'), ('INR', 'INR - Indian Rupee'), ('IQD', 'IQD - Iraqi Dinar'), ('IRR', 'IRR - Iranian Rial'), ('ISK', 'ISK - Iceland Krona'), ('JMD', 'JMD - Jamaican Dollar'), ('JOD', 'JOD - Jordanian Dinar'), ('JPY', 'JPY - Yen'), ('KES', 'KES - Kenyan Shilling'), ('KGS', 'KGS - Som'), ('KHR', 'KHR - Riel'), ('KMF', 'KMF - Comoro Franc'), ('KPW', 'KPW - North Korean Won'), ('KRW', 'KRW - Won'), ('KWD', 'KWD - Kuwaiti Dinar'), ('KYD', 'KYD - Cayman Islands Dollar'), ('KZT', 'KZT - Tenge'), ('LAK', 'LAK - Kip'), ('LBP', 'LBP - Lebanese Pound'), ('LKR', 'LKR - Sri Lanka Rupee'), ('LRD', 'LRD - Liberian Dollar'), ('LSL', 'LSL - Loti'), ('LYD', 'LYD - Libyan Dinar'), ('MAD', 'MAD - Moroccan Dirham'), ('MDL', 'MDL - Moldovan Leu'), ('MGA', 'MGA - Malagasy Ariary'), ('MKD', 'MKD - Denar'), ('MMK', 'MMK - Kyat'), ('MNT', 'MNT - Tugrik'), ('MOP', 'MOP - Pataca'), ('MRO', 'MRO - Ouguiya'), ('MUR', 'MUR - Mauritius Rupee'), ('MVR', 'MVR - Rufiyaa'), ('MWK', 'MWK - Malawi Kwacha'), ('MXN', 'MXN - Mexican Peso'), ('MYR', 'MYR - Malaysian Ringgit'), ('MZN', 'MZN - Mozambique Metical'), ('NAD', 'NAD - Namibia Dollar'), ('NGN', 'NGN - Naira'), ('NIO', 'NIO - Cordoba Oro'), ('NOK', 'NOK - Norwegian Krone'), ('NPR', 'NPR - Nepalese Rupee'), ('NZD', 'NZD - New Zealand Dollar'), ('OMR', 'OMR - Rial Omani'), ('PAB', 'PAB - Balboa'), ('PEN', 'PEN - Sol'), ('PGK', 'PGK - Kina'), ('PHP', 'PHP - Philippine Peso'), ('PKR', 'PKR - Pakistan Rupee'), ('PLN', 'PLN - Zloty'), ('PYG', 'PYG - Guarani'), ('QAR', 'QAR - Qatari Rial'), ('RON', 'RON - Romanian Leu'), ('RSD', 'RSD - Serbian Dinar'), ('RUB', 'RUB - Russian Ruble'), ('RWF', 'RWF - Rwanda Franc'), ('SAR', 'SAR - Saudi Riyal'), ('SBD', 'SBD - Solomon Islands Dollar'), ('SCR', 'SCR - Seychelles Rupee'), ('SDG', 'SDG - Sudanese Pound'), ('SEK', 'SEK - Swedish Krona'), ('SGD', 'SGD - Singapore Dollar'), ('SHP', 'SHP - Saint Helena Pound'), ('SLL', 'SLL - Leone'), ('SOS', 'SOS - Somali Shilling'), ('SRD', 'SRD - Surinam Dollar'), ('SSP', 'SSP - South Sudanese Pound'), ('STD', 'STD - Dobra'), ('SVC', 'SVC - El Salvador Colon'), ('SYP', 'SYP - Syrian Pound'), ('SZL', 'SZL - Lilangeni'), ('THB', 'THB - Baht'), ('TJS', 'TJS - Somoni'), ('TMT', 'TMT - Turkmenistan New Manat'), ('TND', 'TND - Tunisian Dinar'), ('TOP', 'TOP - Pa’anga'), ('TRY', 'TRY - Turkish Lira'), ('TTD', 'TTD - Trinidad and Tobago Dollar'), ('TWD', 'TWD - New Taiwan Dollar'), ('TZS', 'TZS - Tanzanian Shilling'), ('UAH', 'UAH - Hryvnia'), ('UGX', 'UGX - Uganda Shilling'), ('UYU', 'UYU - Peso Uruguayo'), ('UZS', 'UZS - Uzbekistan Sum'), ('VEF', 'VEF - Bolívar'), ('VND', 'VND - Dong'), ('VUV', 'VUV - Vatu'), ('WST', 'WST - Tala'), ('XAF', 'XAF - CFA Franc BEAC'), ('XCD', 'XCD - East Caribbean Dollar'), ('XOF', 'XOF - CFA Franc BCEAO'), ('XPF', 'XPF - CFP Franc'), ('YER', 'YER - Yemeni Rial'), ('ZAR', 'ZAR - Rand'), ('ZMW', 'ZMW - Zambian Kwacha'), ('ZWL', 'ZWL - Zimbabwe Dollar')], max_length=3)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='users.profile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='profilecurrency',
            constraint=models.UniqueConstraint(fields=('currency', 'profile'), name='unique_currency_per_profile'),
        ),
    ]
