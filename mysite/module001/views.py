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
        'prev_page': 'index',
        'next_url': 'page002module001',
        'next_page': 'looking for waste',
    }

    return render(request, 'valueandwaste/page001.html', context)


def page002module001(request):
    """ A view to return page002 """
    context = {
        'arrows': 'arrows',
        'nexthedden': 'true',
        'prev_url': 'page001module001',
        'prev_page': 'background',
        'next_url': 'page003module001',
        'next_page': 'definition of value and waste',
    }

    return render(request, 'valueandwaste/page002.html', context)


def page003module001(request):
    """ A view to return page002 """
    context = {
        'arrows': 'arrows',
        'nexthedden': 'true',
        'prev_url': 'page002module001',
        'prev_page': 'looking for waste',
        'next_url': 'page004module001',
        'next_page': 'examples of value',
    }

    return render(request, 'valueandwaste/page003.html', context)


def page004module001(request):
    """ A view to return page002 """
    context = {
        'arrows': 'arrows',
        'nexthedden': 'true',
        'prev_url': 'page003module001',
        'prev_page': 'definition of value and waste',
        'next_url': 'valueandwaste',
        'next_page': 'index',
    }

    return render(request, 'valueandwaste/page004.html', context)
