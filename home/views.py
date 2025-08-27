from django.shortcuts import render

def homepage(request):
    restaurant = Restaurant.objects.first()
    if restaurant and restaurant.name:
        restaurant_name = restaurant.name
    else:
        restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'Restaurant')

    # get phone number also 
    phone_number = restaurant.phone_number if restaurant and restaurant.phone_number else "Not Available"
    response = requests.get("http://127.0.0.1:8000/api/manu/")
    menu_items = response.json()
    return render(request, 'home/index.html',{'restaurant_name': restaurant_name, 'phone_number': phone_number, "nemu_items": menu_items})

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