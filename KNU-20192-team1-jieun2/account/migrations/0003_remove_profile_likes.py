# Generated by Django 2.2.3 on 2019-12-07 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
    ]