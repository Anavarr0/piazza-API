# Generated by Django 3.0.2 on 2021-04-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0033_auto_20210417_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
