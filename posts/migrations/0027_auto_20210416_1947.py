# Generated by Django 3.0.2 on 2021-04-16 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0026_post_is_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='expiration_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
