from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """
    context = {
        'arrows': 'noarrows',
        'nexthedden': 'false',
    }

    return render(request, 'valueandwaste/intro.html', context)


def page001module001(request):
    """ A view to return page001 """
    context = {
        'arrows': 'arrows',
        'nexthedden': 'false',
        'prev_url': 'valueandwaste',
        'prev_page': 'intro',
        'next_url': 'page002module001',
        'next_page': 'page2',
    }

    return render(request, 'valueandwaste/page001.html', context)


def page002module001(request):
    """ A view to return page002 """
    context = {
        'arrows': 'arrows',
        'nexthedden': 'true',
        'prev_url': 'page001module001',
        'prev_page': 'page1',
        'next_url': 'valueandwaste',
        'next_page': 'page3',
    }

    return render(request, 'valueandwaste/page002.html', context)
