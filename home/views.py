from django.shortcuts import render

def homepage(request):
    restaurant = Restaurant.objects.first()
    if restaurant and restaurant.name:
        restaurant_name = restaurant.name
    else:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Restaurant')
    return render(request, 'home/index.html',{'restaurant_name': restaurant_name})