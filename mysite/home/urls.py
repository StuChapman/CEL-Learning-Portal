from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('group_curo', views.group_curo, name='group_curo'),
]
