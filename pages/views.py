from django.shortcuts import render

# Create your views here.


def view_code(request):
    """ render the code to page """

    return render(request, 'code_display.html')
