# Generated by Django 2.2.2 on 2019-07-03 02:35

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20190702_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='D:\\Pictures\x02.png', storage=django.core.files.storage.FileSystemStorage(location='media/posts'), upload_to=''),
            preserve_default=False,
        ),
    ]