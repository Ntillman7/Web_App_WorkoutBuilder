# Generated by Django 2.2.5 on 2023-08-16 23:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutTracker', '0002_auto_20230816_1629'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='workoutinformation',
            managers=[
                ('information', django.db.models.manager.Manager()),
            ],
        ),
    ]
