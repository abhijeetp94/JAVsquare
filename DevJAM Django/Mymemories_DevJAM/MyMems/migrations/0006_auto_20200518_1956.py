# Generated by Django 3.0.3 on 2020-05-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyMems', '0005_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_details',
            old_name='images',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='notes',
        ),
        migrations.AddField(
            model_name='user_details',
            name='about',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
