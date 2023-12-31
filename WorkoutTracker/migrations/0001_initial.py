# Generated by Django 2.2.5 on 2023-08-16 18:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('workout_type', models.CharField(choices=[('Back and Bis', 'Back and Bis'), ('Chest and Tris', 'Chest and Tris'), ('Quad Focused Legs', 'Quad Focused Legs'), ('Glute Focused Legs', 'Glute Focused Legs'), ('Shoulders', 'Shoulders'), ('Cardio', 'Cardio'), ('Lower body', 'Lower body'), ('Upper Body and core', 'Upper Body and core'), ('Active rest and recovery', 'Active rest and recovery'), ('Lower body with a focus on glutes', 'Lower body with a focus on glutes'), ('Upper body', 'Upper body'), ('Rest and recovery', 'Rest and recovery')], max_length=60, null=True)),
                ('exercise_1', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_2', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_3', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_4', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_5', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_6', models.CharField(blank=True, max_length=60, null=True)),
                ('exercise_7', models.CharField(blank=True, max_length=60, null=True)),
                ('sets', models.PositiveIntegerField(default=0)),
                ('reps', models.CharField(choices=[('0', '0'), ('5', '5'), ('8', '8'), ('10', '10'), ('12', '12'), ('15', '15'), ('20', '20')], default=0, max_length=2)),
                ('cardio', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False, verbose_name='Cardio?')),
                ('cardio_duration', models.CharField(blank=True, max_length=10, null=True)),
            ],
            managers=[
                ('Workouts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutFavorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutTracker.Workout')),
            ],
        ),
    ]
