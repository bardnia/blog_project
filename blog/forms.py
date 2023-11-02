from django import forms
from .models import Post, Comment, Tag

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)