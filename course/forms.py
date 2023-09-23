from django import forms
from .models import CourseAttribute, Comment


class CourseAttributeForm(forms.ModelForm):
    class Meta:
        model = CourseAttribute
        fields = ['key', 'value']


class CommentForm(forms.ModelForm):
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['name', 'phone', 'email', 'message']
