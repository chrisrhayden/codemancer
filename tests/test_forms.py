from snippets import forms, models
import pytest


pytestmark = pytest.mark.django_db


class TestSnippetForm:
    def test_form(self):
        form = forms.SnippetForm(data={})
        assert form.is_valid() is False, '.is_valid validating empted data'

        data = {'': ''}
        form = forms.SnippetForm(data=data)

        assert form.is_valid() is False, '.is_valid is validating empty string'
        assert 'author' not in form.errors, 'author is in errors but can be empty'
        assert 'title' in form.errors, 'title is not in errors'
        assert 'code' in form.errors, 'code is not in errors'
        assert 'language' in form.errors, 'language is not in errors'


        models.Language.objects.create(
                name='elvish', version='beta', base_doc_url='www.tolken.com')

        data = {'author': '',
                'title': 'this is a title',
                'code': 'this is code homie',
                'language': ['1']}
        form = forms.SnippetForm(data=data)
        assert form.is_valid() is True, 'Full Form has errors'


class TestCommentForm:
    def test_form(self):
        data = {'': ''}
        form = forms.CommentForm(data=data)
        assert form.is_valid() is False, 'Validating empty info'

        assert 'text' in form.errors, '"text" form is not in errors'

        data = {'text': 'this is text'}
        form = forms.CommentForm(data=data)

        assert form.is_valid() is True, 'Not validating regular text'


class TestAnnotationForm:
    def test_form(self):
        data = {'': ''}
        form = forms.AnnotationForm(data=data)
        assert form.is_valid() is False, 'Validating empty info'

        assert 'code' in form.errors, '"code" form is not in errors'
        assert 'line_begin' in form.errors, '"line_begin" form is not in errors'
        assert 'line_end' in form.errors, '"line_end" form is not in errors'

        data = {'code': 'this is code',
                'line_begin': 1,
                'line_end': 2}
        form = forms.AnnotationForm(data=data)

        assert form.is_valid() is True, 'Not validating regular text'
