from django.shortcuts import render
from restaurant_management.utils.validation_utils import is_valid_email  

def regester_user(request):
    email = request.POST.get("email")
    if not is_valid_email(email):
        return JsonResponse({"error": "Invalid email"}, status=400)