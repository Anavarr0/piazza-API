# Generated by Django 3.0.2 on 2021-04-15 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_remove_post_expiration_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expiration_time',
            field=models.DurationField(default=datetime.timedelta(0, 120)),
        ),
    ]
