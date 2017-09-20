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
        widgets = {
                'text': forms.Textarea(attrs={'cols': 40, 'rows': 6}),
                'placeholder': 'this is'
        }


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ('code', 'line_begin', 'line_end')

        widgets = {'code': forms.Textarea(attrs={'placeholder': 'type shit here'})}
