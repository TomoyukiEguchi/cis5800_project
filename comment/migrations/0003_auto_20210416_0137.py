# Generated by Django 3.2 on 2021-04-16 05:37

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='full_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
