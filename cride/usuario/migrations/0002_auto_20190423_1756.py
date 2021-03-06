# Generated by Django 2.2 on 2019-04-23 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_client',
            field=models.BooleanField(default=True, help_text='Help easily distinguish users and perform queries. Clients are the main type of user.', verbose_name='client'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_verfied',
            field=models.BooleanField(default=True, help_text='Set to true when the user have verified its email address.', verbose_name='verified'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
