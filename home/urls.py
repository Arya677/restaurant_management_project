from django.urls import path
from .views import *

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.restaurant_about, name="restaurant_about"),
]