# Generated by Django 3.0.2 on 2021-04-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_auto_20210416_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.TimeField(default='00:02:00'),
        ),
    ]
