from django.shortcuts import (render, get_object_or_404)
from snippets.models import Snippet

# Create your views here.


def login_page(request):
    """ a page to login or sign up """

    return render(request, 'login.html')


def code_pasting(request):
    """ paste code on this page """

    return render(request, 'code_pasting.html')


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
