# Generated by Django 3.0.2 on 2020-02-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zing_it', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='song',
            name='lyrics',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
