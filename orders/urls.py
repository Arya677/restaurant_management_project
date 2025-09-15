from django.urls import path
from .views import *

urlpatterns = [
    path('order/', views.order_page, name="order"),
]