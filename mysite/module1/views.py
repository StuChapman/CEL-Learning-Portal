from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def intromodule1(request):
    """ A view to return the intro page """

    return render(request, 'valueandwaste/intro.html')


def backgroundmodule1(request):
    """ A view to return the intro page """

    return render(request, 'valueandwaste/background.html')
    