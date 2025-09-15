from django.shortcuts import render

def order_page(request):
    return render(request, "order.html

def order_confirmation(request):
    order_number = random.random.randit(1000.99999)
    return render(request, "order_confirmation.html", {"order_number": order_number})