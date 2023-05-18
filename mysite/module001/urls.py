from django.urls import path
from . import views

urlpatterns = [
    path('module001/', views.valueandwaste, name='valueandwaste'),
    path('module001/page001module001', views.page001module001, name='page001module001'),
]
