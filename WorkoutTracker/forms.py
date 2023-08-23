from django.forms import ModelForm
from django import forms
from .models import Workout


class WorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = "__all__"


