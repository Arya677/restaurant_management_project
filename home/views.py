from django.shortcuts import render

def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant and restaurant_name esle getattr(setting,'RESTAURANT_NAME', 'Restaurant')
    phone_number = restaurant.phone_number if restaurant and hasattr(restaurant,'phone_number') and restaurant.phone_number esle "Not Available"
    address = restaurant.address if restaurant and hasattr(restaurant,'address') else "Address Not Available"
    try:
        response = requests.get("http://127.0.0.1:8000/api/manu/")
        response.raise_for_status()
        menu_items = response.json()
    except requests.exceptions.RequestException:
        menu_items = []
            
    return render(request, 'home/index.html',{'restaurant_name': restaurant_name, 'phone_number': phone_number, "nemu_items": menu_items}, "address":address)

def menu_page(request):
    menu_items = MenuItem.objects.all()
    return render(request,'menu/menu.html',{'menu_items': menu_items})

def restaurant_about(request):
    return render(request, 'home/restaurant_about.html')

def reservations import render:
    return render(request, 'reservations.html')

def feedback_view(request):
    if request.method == 'POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request,'menu.html',{'menu_items':menu_items})