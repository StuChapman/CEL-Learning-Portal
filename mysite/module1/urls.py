from django.urls import path
from . import views

urlpatterns = [
    path('module1/', views.valueandwaste, name='valueandwaste'),
    path('module1/backgroundmodule1', views.backgroundmodule1, name='backgroundmodule1'),
]
