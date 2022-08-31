# Generated by Django 4.1 on 2022-08-30 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="CRN",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("quarter", models.CharField(max_length=2)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedules.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Timeslot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.TimeField(max_length=20)),
                ("end_time", models.TimeField(max_length=20)),
                ("campus", models.CharField(max_length=5)),
                ("room", models.CharField(max_length=50)),
                (
                    "crn",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schedules.crn"
                    ),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schedules.instructor",
                    ),
                ),
            ],
        ),
    ]
