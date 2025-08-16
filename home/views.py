from django.shortcuts import render

def homepage(request):
    restaurant = Restaurant.objects.first()
    if restaurant and restaurant.name:
        restaurant_name = restaurant.name
    else:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Restaurant')

    # get phone number also 
    phone_number = restaurant.phone_number if restaurant and restaurant.phone_number else "Not Available"

    return render(request, 'home/index.html',{'restaurant_name': restaurant_name, 'phone_number': phone_number})

def restaurant_about(request):
    return render(request, 'home/restaurant_about.html')