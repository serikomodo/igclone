# Generated by Django 2.2.2 on 2019-07-02 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190702_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='user_following',
            new_name='user_follower',
        ),
    ]