from django.urls import path
from .views import *

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.restaurant_about, name="restaurant_about"),
    path('menu/', views.menu_list, name="menu_list"),
    path('contact/', views.contact_us, name='contact_us'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('api/', include("rest.urls")),
    path('contact/', views.contact_view, name="contact"),
    path("faq/", views.faq_view. name="faq"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy")
    path('api/contact/', ContactSubmissionView.as_view(), name='contact=form'),
] if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                                  )