import re
import pytest
from django.test import RequestFactory
from django.utils import timezone
from mixer.backend.django import mixer
from snippets.models import Language, Comment
from pages.views import (landing_page, login_page,
                         create_snippet, snippet_detail, snippet_change)


pytestmark = pytest.mark.django_db


class TestLandingPage:
    def test_view(self):
        obj = mixer.blend('snippets.Snippet')

        com_data = {'author': None, 'created': timezone.now(),
                    'snippet': obj, 'text': 'this is text'}
        c = Comment.objects.create(**com_data)

        request = RequestFactory().get('/')
        response = landing_page(request)

        patt = re.compile(r'[45]\d+')
        assert patt.match(str(response.status_code)) is None, 'landing_page not calling'

        assert response.status_code == 200, 'not calling'


class TestLoginPage:
    def test_view(self):

        request = RequestFactory().get('/')
        response = login_page(request)

        patt = re.compile(r'[45]\d+')
        assert patt.match(str(response.status_code)) is None, 'login_page not calling'
        assert response.status_code == 200, 'not calling'


class TestCreateSnippet:
    def test_view(self):

        request = RequestFactory().get('/')
        response = create_snippet(request)

        patt = re.compile(r'[45]\d+')
        assert patt.match(str(response.status_code)) is None, 'create_snippet not calling'
        assert response.status_code == 200, 'not calling'

    def test_view_post(self):

        obj = mixer.blend('snippets.Snippet')

        lang_data = {'name': 'testish', 'version': 'very first',
                     'base_doc_url': 'www.superrad.com'}

        l = Language.objects.create(**lang_data)

        data = {'author': '', 'title': 'this is a title',
                'code': 'this is code', 'created': timezone.now(),
                'language': l.pk}

        request = RequestFactory().post('/', data=data)
        response = create_snippet(request)

        assert response.status_code == 302, 'not posting'


class TestSnippetDeatail:
    def test_view(self):
        obj = mixer.blend('snippets.Snippet')

        com_data = {'author': None, 'created': timezone.now(),
                    'snippet': obj, 'text': 'this is text'}
        com = mixer.blend('snippets.Comment', **com_data)

        request = RequestFactory().get('/')
        response = snippet_detail(request, obj.pk)

        patt = re.compile(r'[45]\d+')
        assert patt.match(str(response.status_code)) is None, 'login_page not calling'
        assert response.status_code == 200, 'not calling'

    def test_view_post(self):

        obj = mixer.blend('snippets.Snippet')

        com_data = {'author': None, 'created': timezone.now(),
                    'snippet': obj, 'text': 'this is text'}

        # com = mixer.blend('snippets.Comment', =com_data)

        request = RequestFactory().post('/', data=com_data)
        response = snippet_detail(request, obj.pk)

        com = Comment.objects.get(id=1)
        assert com, 'no comment'
        assert response.status_code == 200, f'response code is {response.status_code}'


class TestSnippetChange:
    def test_view(self):

        obj = mixer.blend('snippets.Snippet')
        pk = obj.pk

        request = RequestFactory().get('/')
        response = snippet_change(request, pk)

        assert response.status_code == 200, f'response code {response.status_code}'

    def test_view_post(self):

        obj = mixer.blend('snippets.Snippet')

        lang_data = {'name': 'testish', 'version': 'very first',
                     'base_doc_url': 'www.superrad.com'}

        lang = Language.objects.create(**lang_data)

        data = {'author': '', 'title': 'this is a title',
                'code': 'this is code', 'created': timezone.now(),
                'language': lang.pk}

        request = RequestFactory().post('/', data=data)
        response = snippet_change(request, obj.pk)

        assert response.status_code == 302, 'response code {response.status_code}'
