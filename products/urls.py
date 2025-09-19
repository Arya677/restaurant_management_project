from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),                               
    path("api/menu/category/", menu_items_by_category, name='menu-items-by-cayegpory')
    path("api/menu/search", MenuItemSearchViewSet, name="menu-item-search" )
]