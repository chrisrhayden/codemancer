from django import forms
from .models import (Snippet, Comment, Annotation)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('author', 'title', 'code', 'language')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ('code', 'line_begin', 'line_end')
