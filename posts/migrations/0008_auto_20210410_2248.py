# Generated by Django 3.0.2 on 2021-04-10 22:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210410_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 12, 22, 48, 1, 211006, tzinfo=utc)),
        ),
    ]
