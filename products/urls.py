from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("api/menu/category/", menu_items_by_category, name='menu-items-by-cayegpory')