# Generated by Django 3.0.3 on 2020-05-18 06:22

import MyMems.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='images',
            field=models.ImageField(default='', upload_to=MyMems.models.get_image_path),
        ),
        migrations.AddField(
            model_name='user_details',
            name='notes',
            field=models.FileField(default='', upload_to=MyMems.models.get_upload_path),
        ),
    ]
