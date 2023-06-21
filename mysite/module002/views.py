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
            return render(request, 'dampandmould/page001.html', context)

        """ create a Page for this user for this page """
        user_page = Pages(user=request.user,
                          page=thispage,
                          status=1,)
        user_page.save()

    return render(request, 'dampandmould/page001.html', context)
