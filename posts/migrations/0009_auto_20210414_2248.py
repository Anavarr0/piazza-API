# Generated by Django 3.0.2 on 2021-04-14 22:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210410_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 16, 22, 48, 0, 143088, tzinfo=utc)),
        ),
    ]
