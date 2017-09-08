from django.shortcuts import (
        render, redirect,
        get_object_or_404)
from snippets.models import (Snippet, Language, Comment)
from snippets.forms import (SnippetForm, CommentForm)

# Create your views here.


def landing_page(request):

    latest = Snippet.objects.latest('created')
    lang = Language.objects.all()

    context = {'latest': latest, 'lang': lang}
    return render(request, 'landing_page.html', context)


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

    lang = Language.objects.order_by('name')
    snippets = Snippet.objects.all()
    context = {'snippets': snippets, 'lang': lang}
    return render(request, 'list_snippets.html', context)


def about(request):
    """ show about page """

    lang = Language.objects.order_by('name')
    context = {'lang': lang}
    return render(request, 'about.html', context)


def snippet_detail(request, pk):
    """ render the code to page

    Show code and add comments
    """

    # old code for posterity
    # snippet = Snippet.objects.get(id=pk)

    snippet = get_object_or_404(Snippet, id=pk)
    lang = Language.objects.order_by('name')
    comments = Comment.objects.filter(snippet=snippet)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.snippet = snippet
            new_comment.save()

    form = CommentForm()
    context = {
            'snippet': snippet,
            'lang': lang,
            'form': form,
            'comments': comments
    }
    return render(request, 'detail.html', context)


def snippet_change(request, pk):
    """ crud, update snippet """

    s = Snippet.objects.get(id=pk)

    if request.method == 'GET':
        form = SnippetForm(instance=s)
    elif request.method == 'POST':
        form = SnippetForm(instates=s, data=request.POST)
        if form.is_valid():
            update_snip = form.save(commit=False)
            update_snip.save()

    s_name = s.title
    context = {'form': form, 'name': s_name}
    return render(request, 'snippet_change.html', context)
