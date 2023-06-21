from django.urls import path
from . import views

urlpatterns = [
    path('module002/', views.dampandmould, name='dampandmould'),
    path('module002/page001module002',
         views.page001module002,
         name='page001module002'),
    path('module002/page002module002',
         views.page002module002,
         name='page002module002'),
    path('module002/page003module002',
         views.page003module002,
         name='page003module002'),
    path('module002/page004module002',
         views.page004module002,
         name='page004module002'),
]
