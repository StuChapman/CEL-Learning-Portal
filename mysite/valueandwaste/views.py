from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def introvalueandwaste(request):
    """ A view to return the intro page """

    return render(request, 'valueandwaste/intro.html')
