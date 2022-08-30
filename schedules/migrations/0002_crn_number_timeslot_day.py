# Generated by Django 4.1 on 2022-08-30 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crn',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslot',
            name='day',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
