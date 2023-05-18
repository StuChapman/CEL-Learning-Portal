from django.urls import path
from . import views

urlpatterns = [
    path('module1/', views.intromodule1, name='intromodule1'),
    path('module1/backgroundmodule1', views.backgroundmodule1, name='backgroundmodule1'),
]
