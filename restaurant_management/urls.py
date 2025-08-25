from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html',status=404)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/',include('home.urls')),
    path('api/accounts/',include('account.urls')),
    path('api/products/',include('products.urls')),
    path('api/orders/',include('orders.urls')),
    path('api/', include(rest.urls)),

]

handler404 = 'restaurant_management.urls.custom_404'