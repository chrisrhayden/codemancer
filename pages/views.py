from django.shortcuts import (
        render, redirect,
        get_object_or_404)
from rest_framework import viewsets
from snippets.models import (Snippet, Language, Comment, Annotation)
from snippets.forms import (SnippetForm, CommentForm, AnnotationForm)
from snippets.serializers import LanguageSerializer, AnnotationSerializer

# Create your views here.


def landing_page(request):
    """ get the latest snippet and its comment """

    latest = Snippet.objects.latest('created')
    comment = Comment.objects.filter(snippet=latest)
    code_lines = latest.code.split('\n')

    if comment:
        comment = comment.latest('created')
        context = {
                'latest': latest,
                'comment': comment,
                'code_lines': code_lines,
        }
    else:
        comment_form = CommentForm()
        context = {
                'latest': latest,
                'code_lines': code_lines,
                'comment_form': comment_form,
        }

    return render(request, 'landing_page.html', context)


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """ for api """

    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    """ for api """

    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


def login_page(request):
    """ a page to login or sign up """

    lang = Language.objects.order_by('name')
    context = {'lang': lang}
    return render(request, 'login.html', context)


def create_snippet(request):
    """ paste code on this page """

    if request.method == 'GET':
        form = SnippetForm()

    elif request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snip_post = form.save(commit=False)  # return instates

#            code_list = list()
#            code = snip_post.code.split('\n')
#            for i, line in enumerate(code, 1):
#                this = f'{i}'.zfill(2) + ' ' + line
#                code_list.append(this)
#
#            snip_post.code = '\n'.join(code_list)

            snip_post.save()                     # now save
            form.save_m2m()
            # send to display view (below)
            # using url related name
            return redirect('snippet_detail',
                            pk=snip_post.id)

    lang = Language.objects.order_by('name')
    context = {'form': form, 'lang': lang}
    return render(request, 'create.html', context)


def list_snippets(request):
    """ a page with all snipts in a list """

    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'list_snippets.html', context)


def snippet_detail(request, pk):
    """ render the code to page

    Show code and add comments
    """

    # old code for posterity
    # snippet = Snippet.objects.get(id=pk)
    snippet = get_object_or_404(Snippet, id=pk)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.snippet = snippet
            new_comment.save()

    code_lines = snippet.code.split('\n')

    comments = Comment.objects.filter(snippet=snippet)
    annotations = Annotation.objects.filter(snippet=snippet)

    form = CommentForm()
    ano_form = AnnotationForm()

    context = {
            'snippet': snippet,
            'annotations': annotations,
            'code_lines': code_lines,
            'form': form,
            'ano_form': ano_form,
            'comments': comments,
    }
    return render(request, 'detail.html', context)


def snippet_change(request, pk):
    """ crud, update snippet """

    s = Snippet.objects.get(id=pk)

    if request.method == 'GET':
        form = SnippetForm(instance=s)
    elif request.method == 'POST':
        form = SnippetForm(instance=s, data=request.POST)
        if form.is_valid():
            update_snip = form.save(commit=False)
            update_snip.save()
            return redirect('snippet_detail',
                            pk=update_snip.id)

    s_name = s.title
    context = {'form': form, 'name': s_name}
    return render(request, 'snippet_change.html', context)
