from django.shortcuts import render

def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant and restaurant_name esle getattr(setting,'RESTAURANT_NAME', 'Restaurant')
    phone_number = restaurant.phone_number if restaurant and hasattr(restaurant,'phone_number') and restaurant.phone_number esle "Not Available"
    address = restaurant.address if restaurant and hasattr(restaurant,'address') else "Address Not Available"
    current_time = timezone.locaktime(timezone.now())
    try:
        response = requests.get("http://127.0.0.1:8000/api/manu/")
        response.raise_for_status()
        menu_items = response.json()
    except requests.exceptions.RequestException:
        menu_items = []

    query = request.GET.get("q","")
    if qyery:
        menu_items = [item for item in menu_items if query.lower() in item.get("name","").lower()]
            
    return render(request, 'home/index.html',{'restaurant_name': restaurant_name, 'phone_number': phone_number, "nemu_items": menu_items, "current_time": current_time}, "address":address, "query":query )

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

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleanedata["name"]
            email = form.cleanedata["email"]
            message = form.cleanedata["message"]

            subject = f"New Contact Message from {name}"
            full_message = f"Name" {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            send_mail(
                subject,
                full_message,
                setting.DEFAULT_FORM_EMAIL,
                ["restaurant_email@examole.com"],
            )
            return redirect("contact_success")
    else:
        form.ContactForm()
            return redirect("contact")
    return render(request,"home/contact.html",{"form": form})

    