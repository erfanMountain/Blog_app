from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # Here comma is added because we can add more comma later on
        fields = ('text',)