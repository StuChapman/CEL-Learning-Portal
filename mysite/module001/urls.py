from django.urls import path
from . import views

urlpatterns = [
    path('module001/', views.valueandwaste, name='valueandwaste'),
    path('module001/page001module001', 
        views.page001module001, 
            name='page001module001'),
    path('module001/page002module001', views.page002module001, name='page002module001'),
    path('module001/page003module001', views.page003module001, name='page003module001'),
    path('module001/page004module001', views.page004module001, name='page004module001'),
    path('module001/page005module001', views.page005module001, name='page005module001'),
    path('module001/page006module001', views.page006module001, name='page006module001'),
]
