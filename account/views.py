from django.shortcuts import render
from restaurant_management.utils.validation_utils import is_valid_email  
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserUpdateSerializer

class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permissions_class = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

def regester_user(request):
    email = request.POST.get("email")
    if not is_valid_email(email):
        return JsonResponse({"error": "Invalid email"}, status=400)