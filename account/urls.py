from django.urls import path
from .views import *

urlpatterns = [
    path('profile/update/',UserProfileUpdateView.as_view(), name="profile-update"),        
]