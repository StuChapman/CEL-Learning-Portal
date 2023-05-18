from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """

    return render(request, 'valueandwaste/intro.html')


def page001module001(request):
    """ A view to return page001 """

    return render(request, 'valueandwaste/page001.html')
    