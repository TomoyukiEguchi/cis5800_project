# Generated by Django 3.2 on 2021-05-03 00:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20210502_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='guest',
            field=models.CharField(choices=[('', 'Choose...'), ('2', '2 Guests'), ('3', '3 Guests'), ('4', '4 Guests'), ('5+', '5+ Guests')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]