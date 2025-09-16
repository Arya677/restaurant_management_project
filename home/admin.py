from django.contrib import admin
from .models import Menu, Order, MenuItem, Restaurant, UserProfile, MenuCategory               

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(MenuCategory)
admin.site.register(UserProfile)

@admin.register(MenuItem)
class MenuItemAdmin(admin,ModelAdmin):
    list_display = ('name','price','image')

@admin.register(Restaurant):
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_number')