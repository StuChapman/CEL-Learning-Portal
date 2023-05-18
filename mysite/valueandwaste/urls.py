from django.urls import path
from . import views

urlpatterns = [
    path('valueandwaste/', views.introvalueandwaste, name='introvalueandwaste'),
]
