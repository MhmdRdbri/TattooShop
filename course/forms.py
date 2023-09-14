from django import forms
from .models import CourseAttribute


class CourseAttributeForm(forms.ModelForm):
    class Meta:
        model = CourseAttribute
        fields = ['key', 'value']
