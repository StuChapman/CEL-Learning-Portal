from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from django.utils.safestring import mark_safe
from . import views
from .models import Pages, Tests, Answers

# Create your views here.


def dampandmould(request):
    """ A view to return the intro page """
    thispage = 'dampandmould'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'dampandmould/intro.html', context)


def page001module002(request):
    """ A view to return page001 """
    thispage = 'page001module002'
    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': 'false',
        'prev_url': 'dampandmould',
        'prev_page': 'index',
        'prev_page_small': 'index',
        'next_url': 'page002module002',
        'next_page': 'what is condensation?',
        'next_page_small': 'condensation',
    }

    if request.user.is_authenticated:
        """ check if a Page exists for this user for this page """
        pages = Pages.objects.all()
        page_exists = (pages.filter
                       (user=request.user,
                        page=thispage,
                        status=1,))
        if page_exists:
            return render(request, 'dampandmould/page001.html', context)

        """ create a Page for this user for this page """
        user_page = Pages(user=request.user,
                          page=thispage,
                          status=1,)
        user_page.save()

    return render(request, 'dampandmould/page001.html', context)


def page002module002(request):
    """ A view to return page002 """
    thispage = 'page002module002'

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
        'prev_url': 'page001module002',
        'prev_page': 'background',
        'prev_page_small': 'background',
        'next_url': 'page003module002',
        'next_page': 'condensation in the home',
        'next_page_small': 'home condensation',
    }
    return render(request, 'dampandmould/page002.html', context)


def page003module002(request):
    """ A view to return page003 """
    thispage = 'page003module002'

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
        'prev_url': 'page002module002',
        'prev_page': 'what is condensation?',
        'prev_page_small': 'condensation',
        'next_url': 'page004module002',
        'next_page': 'sources of condensation',
        'next_page_small': 'sources',
    }
    return render(request, 'dampandmould/page003.html', context)


def page004module002(request):
    """ A view to return page004 """
    thispage = 'page004module002'

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
        'prev_url': 'page003module002',
        'prev_page': 'condensation in the home',
        'prev_page_small': 'home condensation',
        'next_url': 'page005module002',
        'next_page': 'ventilation',
        'next_page_small': 'ventilation',
    }
    return render(request, 'dampandmould/page004.html', context)


def page005module002(request):
    """ A view to return page005 """
    thispage = 'page005module002'

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
        'prev_url': 'page004module002',
        'prev_page': 'sources of condensation',
        'prev_page_small': 'sources',
        'next_url': 'page006module002',
        'next_page': 'measuring humidity',
        'next_page_small': 'humidity',
    }
    return render(request, 'dampandmould/page005.html', context)


def page006module002(request):
    """ A view to return page006 """
    thispage = 'page006module002'

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
            """ specific to this page only """
            nexthidden = 'false'

    context = {
        'thispage': thispage,
        'arrows': 'arrows',
        'nexthidden': nexthidden,
        'prev_url': 'page005module002',
        'prev_page': 'ventilation',
        'prev_page_small': 'ventilation',
        'next_url': 'page007module002',
        'next_page': 'managing humidity',
        'next_page_small': 'humidity',
    }
    return render(request, 'dampandmould/page006.html', context)


def page007module002(request):
    """ A view to return page007 """
    thispage = 'page007module002'

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
        'prev_url': 'page006module002',
        'prev_page': 'measuring humidity',
        'prev_page_small': 'humidity',
        'next_url': 'page008module002',
        'next_page': 'cold surfaces',
        'next_page_small': 'cold surfaces',
    }
    return render(request, 'dampandmould/page007.html', context)


def page008module002(request):
    """ A view to return page008 """
    thispage = 'page008module002'

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
        'prev_url': 'page007module002',
        'prev_page': 'managing humidity',
        'prev_page_small': 'humidity',
        'next_url': 'page009module002',
        'next_page': 'damp & mould survey',
        'next_page_small': 'survey',
    }
    return render(request, 'dampandmould/page008.html', context)


def page009module002(request):
    """ A view to return page009 """
    thispage = 'page009module002'

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
        'prev_url': 'page008module002',
        'prev_page': 'cold surfaces',
        'prev_page_small': 'cold surfaces',
        'next_url': 'testintro',
        'next_page': 'test',
        'next_page_small': 'test',
    }
    return render(request, 'dampandmould/page009.html', context)


def testintro(request):
    """ A view to return the testintro page """
    thistest = 'testintro'
    nexttest = 'test001module002'
    context = {
        'thistest': thistest,
        'nexttest': nexttest,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'dampandmould/testintro.html', context)
