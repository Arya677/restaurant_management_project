from django.urls import path
from .views import *

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.restaurant_about, name="restaurant_about"),
    path('menu/', views.menu_list, name="menu_list"),
    path('contact/', views.contact_us, name='contact_us'),
]