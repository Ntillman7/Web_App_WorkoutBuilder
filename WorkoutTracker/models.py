from django.db import models


TYPE_CHOICES = (
    (' ',' '),
    ('Back and Bis', 'Back and Bis'),
    ('Chest and Tris', 'Chest and Tris'),
    ('Quad Focused Legs', 'Quad Focused Legs'),
    ('Glute Focused Legs', 'Glute Focused Legs'),
    ('Shoulders', 'Shoulders'),
    ('Lower body', 'Lower body'),
    ('Upper Body and core', 'Upper Body and core'),
    ('Active rest and recovery', 'Active rest and recovery'),
    ('Lower body with a focus on glutes', 'Lower body with a focus on glutes'),
    ('Upper body', 'Upper body'),
)

CARDIO_CHOICES = [(False, 'No'), (True, 'Yes')]

REP_CHOICES = (
    ('0', '0'),
    ('5', '5'),
    ('8', '8'),
    ('10', '10'),
    ('12', '12'),
    ('15', '15'),
    ('20', '20'),
)


class Workout(models.Model):
    date = models.DateField(auto_now_add=True)
    workout_type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    # default means it starts out empty, blank is ok for forms on webpage, blank(null) is not allowed for database
    exercise_1 = models.CharField(max_length=60, null=True, blank=True)
    exercise_2 = models.CharField(max_length=60, null=True, blank=True)
    exercise_3 = models.CharField(max_length=60, null=True, blank=True)
    exercise_4 = models.CharField(max_length=60, null=True, blank=True)
    exercise_5 = models.CharField(max_length=60, null=True, blank=True)
    exercise_6 = models.CharField(max_length=60, null=True, blank=True)
    exercise_7 = models.CharField(max_length=60, null=True, blank=True)
    sets = models.PositiveIntegerField(default=0)
    reps = models.CharField(max_length=2, choices=REP_CHOICES, default=0)
    cardio = models.BooleanField("Cardio?", default=False, choices=CARDIO_CHOICES)
    cardio_duration = models.CharField(max_length=10, null=True, blank=True)

    Workouts = models.Manager()


class WorkoutFavorites(models.Model):
    item = models.ForeignKey(Workout, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.date


BSTYPE_CHOICES = (
    ('Cardio', 'Cardio'),
    ('Lower body', 'Lower body'),
    ('Upper Body and core', 'Upper Body and core'),
    ('Active rest and recovery', 'Active rest and recovery'),
    ('Lower body with a focus on glutes', 'Lower body with a focus on glutes'),
    ('Upper body', 'Upper body'),
    ('Rest and recovery', 'Rest and recovery'),
 )


class WorkoutInformation(models.Model):
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=60, choices=BSTYPE_CHOICES)
    description = models.TextField(max_length=500, null=True, blank=True)
    duration = models.CharField(max_length=10, null=True, blank=True)
    cardio = models.BooleanField("Cardio?", default=False, choices=CARDIO_CHOICES)
    cardio_duration = models.CharField(max_length=10, null=True, blank=True)

    information = models.Manager()

    def __str__(self):
        return self.description
