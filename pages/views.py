from django.shortcuts import render

# Create your views here.


def login_page(request):
    """ a page to login or sign up """

    return render(request, 'login.html')


def code_pasting(request):
    """ paste code on this page """

    return render(request, 'code_pasting.html')


def list_snippets(request):
    """ a page with all snipts in a list """

    return render(request, 'list_snippets.html')


def about(request):
    """ show about page """

    return render(request, 'about.html')


def view_code(request):
    """ render the code to page """

    return render(request, 'code_display.html')
