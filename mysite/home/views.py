from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth.models import Group

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')


def group_curo(request):
    """ A view to enrol the user in the curo group """

    user = request.user
    g = Group.objects.get(name="Damp and Mould")
    user.groups.add(g)
    user.save()

    return render(request, 'home/home.html')
