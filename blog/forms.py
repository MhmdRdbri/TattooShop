from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Comment
        fields = ['name', 'phone', 'email', 'message']


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=100, required=False)
