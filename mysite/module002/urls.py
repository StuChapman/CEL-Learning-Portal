from django.urls import path
from . import views

urlpatterns = [
    path('module002/', views.dampandmould, name='dampandmould'),
    path('module002/page001module002',
         views.page001module002,
         name='page001module002'),
]