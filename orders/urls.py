from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')                  
  
urlpatterns = [
    path('order/', views.order_page, name="order"),         
    path('<str:order_id/', OrderDeatilView.as_view(), name= "order-detail"),      
    path('api/orders/history/', OrderHistoryView.as_view(), name= "order-history"),
    path('api/', include(router.urls)),
]