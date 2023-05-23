from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """
    context = {
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'valueandwaste/intro.html', context)


def page001module001(request):
    """ A view to return page001 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'false',
        'prev_url': 'valueandwaste',
        'prev_page': 'index',
        'prev_page_small': 'index',
        'next_url': 'page002module001',
        'next_page': 'looking for waste',
        'next_page_small': 'looking',
    }

    return render(request, 'valueandwaste/page001.html', context)


def page002module001(request):
    """ A view to return page002 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page001module001',
        'prev_page': 'background',
        'prev_page_small': 'background',
        'next_url': 'page003module001',
        'next_page': 'definition of value and waste',
        'next_page_small': 'definition',
    }

    return render(request, 'valueandwaste/page002.html', context)


def page003module001(request):
    """ A view to return page003 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page002module001',
        'prev_page': 'looking for waste',
        'prev_page_small': 'looking',
        'next_url': 'page004module001',
        'next_page': 'examples of value',
        'next_page_small': 'value',
    }

    return render(request, 'valueandwaste/page003.html', context)


def page004module001(request):
    """ A view to return page004 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page003module001',
        'prev_page': 'definition of value and waste',
        'prev_page_small': 'definition',
        'next_url': 'page005module001',
        'next_page': 'examples of waste',
        'next_page_small': 'waste',
    }

    return render(request, 'valueandwaste/page004.html', context)


def page005module001(request):
    """ A view to return page005 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page004module001',
        'prev_page': 'examples of value',
        'prev_page_small': 'value',
        'next_url': 'page006module001',
        'next_page': 'necessary non-value-add',
        'next_page_small': 'non-value-add',
    }

    return render(request, 'valueandwaste/page005.html', context)


def page006module001(request):
    """ A view to return page006 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page005module001',
        'prev_page': 'examples of waste',
        'prev_page_small': 'waste',
        'next_url': 'page007module001',
        'next_page': 'the eight wastes',
        'next_page_small': '8 wastes',
    }

    return render(request, 'valueandwaste/page006.html', context)


def page007module001(request):
    """ A view to return page007 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page006module001',
        'prev_page': 'necessary non-value-add',
        'prev_page_small': 'non-value-add',
        'next_url': 'page008module001',
        'next_page': 'example: making a chair',
        'next_page_small': 'example',
    }

    return render(request, 'valueandwaste/page007.html', context)


def page008module001(request):
    """ A view to return page008 """
    context = {
        'arrows': 'arrows',
        'nexthidden': 'true',
        'prev_url': 'page007module001',
        'prev_page': 'the eight wastes',
        'prev_page_small': '8 wastes',
        'next_url': 'valueandwaste',
        'next_page': 'index',
        'next_page_small': 'index',
    }

    return render(request, 'valueandwaste/page008.html', context)
