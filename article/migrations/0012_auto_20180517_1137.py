# Generated by Django 2.0.4 on 2018-05-17 11:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20180517_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 17, 11, 37, 10, 369270, tzinfo=utc)),
        ),
    ]
