# Generated by Django 3.0.2 on 2021-04-17 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0035_dislike_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dislike',
            old_name='liked_post',
            new_name='disliked_post',
        ),
    ]
