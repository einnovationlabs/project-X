# Generated by Django 4.2.3 on 2023-08-18 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='likes',
        ),
    ]
