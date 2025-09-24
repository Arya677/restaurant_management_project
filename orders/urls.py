from django.urls import path
from .views import *

urlpatterns = [
    path('order/', views.order_page, name="order"),  
    path('<str:order_id/', OrderDeatilView.as_view(), name= "order-detail"),      
    path('api/orders/history/', OrderHistoryView.as_view(), name= "order-history"),
]