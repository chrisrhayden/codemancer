from django.shortcuts import (render, redirect, get_object_or_404)
from snippets.models import (Snippet, Language)
from snippets.forms import SnippetForm

# Create your views here.


def login_page(request):
    """ a page to login or sign up """

    lang = Language.objects.order_by('name')
    context = {'lang': lang}
    return render(request, 'login.html', context)


def code_pasting(request):
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
            return redirect('code_display',
                            pk=snip_post.id)

    lang = Language.objects.order_by('name')
    context = {'form': form, 'lang': lang}
    return render(request, 'code_pasting.html', context)


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


def view_code(request, pk):
    """ render the code to page """

    # old code for posterity
    # snippet = Snippet.objects.get(id=pk)

    snippet = get_object_or_404(Snippet, id=pk)
    lang = Language.objects.order_by('name')

    context = {'snippet': snippet, 'lang': lang}
    return render(request, 'code_display.html', context)
