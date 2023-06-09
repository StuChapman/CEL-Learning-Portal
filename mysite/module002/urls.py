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
    path('module002/page005module002',
         views.page005module002,
         name='page005module002'),
    path('module002/page006module002',
         views.page006module002,
         name='page006module002'),
    path('module002/page007module002',
         views.page007module002,
         name='page007module002'),
    path('module002/page008module002',
         views.page008module002,
         name='page008module002'),
    path('module002/page009module002',
         views.page009module002,
         name='page009module002'),
    path('module002/page010module002',
         views.page010module002,
         name='page010module002'),
    path('module002/damptestintro',
         views.damptestintro,
         name='damptestintro'),
    path('module002/dampnexttest',
         views.dampnexttest,
         name='dampnexttest'),
    path('module002/dampcheckanswer',
         views.dampcheckanswer,
         name='dampcheckanswer'),
    path('module002/dampretest',
         views.dampretest,
         name='dampretest'),
    path('module002/damptestcertificate',
         views.damptestcertificate,
         name='damptestcertificate'),
]
