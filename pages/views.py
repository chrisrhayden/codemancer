from django.shortcuts import (render, redirect, get_object_or_404)
from snippets.models import Snippet
from snippets.forms import SnippetForm

# Create your views here.


def login_page(request):
    """ a page to login or sign up """

    return render(request, 'login.html')


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

    context = {'form': form}
    return render(request, 'code_pasting.html', context)


def list_snippets(request):
    """ a page with all snipts in a list """

    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'list_snippets.html', context)


def about(request):
    """ show about page """

    return render(request, 'about.html')


def view_code(request, pk):
    """ render the code to page """

    # old code for posterity
    # snippet = Snippet.objects.get(id=pk)

    snippet = get_object_or_404(Snippet, id=pk)
    context = {'snippet': snippet}
    return render(request, 'code_display.html', context)
