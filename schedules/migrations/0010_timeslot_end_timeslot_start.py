# Generated by Django 4.1 on 2022-08-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0009_alter_instructor_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='end',
            field=models.CharField(default='12:00pm', max_length=20),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='start',
            field=models.CharField(default='9:00am', max_length=20),
        ),
    ]