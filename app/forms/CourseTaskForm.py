from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app.models.CourseTask import CourseTask

class CourseTaskForm(forms.ModelForm):
    class Meta:
        model = CourseTask
        fields = ['course', 'name', 'image', 'level']
        widgets = {
            'course': forms.HiddenInput(),
        }