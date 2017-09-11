import pytest
from mixer.backend.django import mixer
from snippets.forms import SnippetForm


pytestmark = pytest.mark.django_db


class TestSnippet:

    def test_init(self):
        obj = mixer.blend('snippets.Snippet')
        assert obj.pk == 1, 'Cant save, sum thing went wrong in model'

        data = {'author': None}
        form = SnippetForm(data=data)

        assert form.is_valid() is True, 'Author is invalid'
