from django.shortcuts import render
from django.urls import path
from . import views
from .models import Pages

# Create your views here.


def valueandwaste(request):
    """ A view to return the intro page """
    thispage = 'valueandwaste'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'valueandwaste/intro.html', context)


def dummy(request):
    """ A view to return the dummy page """
    thispage = 'dummy'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'valueandwaste/dummy.html', context)


def page001module001(request):
    """ A view to return page001 """
    thispage = 'page001module001'
    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': 'false',
        'prev_url': 'valueandwaste',
        'prev_page': 'index',
        'prev_page_small': 'index',
        'next_url': 'page002module001',
        'next_page': 'looking for waste',
        'next_page_small': 'looking',
    }

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            return render(request, 'valueandwaste/page001.html', context)

        """ create a Page for this user for this page """
        user_page = Pages(user=request.user,
                          page=thispage,
                          status=1,)
        user_page.save()

    return render(request, 'valueandwaste/page001.html', context)


def page002module001(request):
    """ A view to return page002 """
    thispage = 'page002module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page003module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page004module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page005module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page006module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page007module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
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
    thispage = 'page008module001'

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            nexthidden = 'false'
        else:
            """ create a Page for this user for this page """
            user_page = Pages(user=request.user,
                              page=thispage,
                              status=1,)
            user_page.save()
            nexthidden = 'true'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page007module001',
        'prev_page': 'the eight wastes',
        'prev_page_small': '8 wastes',
        'next_url': 'dummy',
        'next_page': 'dummy',
        'next_page_small': 'dummy',
    }
    return render(request, 'valueandwaste/page008.html', context)
