# Generated by Django 2.0.4 on 2018-05-16 14:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20180516_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 14, 4, 58, 852085, tzinfo=utc)),
        ),
    ]
