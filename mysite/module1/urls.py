from django.urls import path
from . import views

urlpatterns = [
    path('module1/', views.valueandwaste, name='valueandwaste'),
    path('module1/page1module1', views.page1module1, name='page1module1'),
]
