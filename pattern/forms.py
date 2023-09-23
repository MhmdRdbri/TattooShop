from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['name', 'phone', 'email', 'message']
