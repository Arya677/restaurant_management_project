from django.contrib import admin
from .models import Menu, Order, MenuItem, Restaurant

admin.site.register(Menu)
admin.site.register(Order)

@admin.register(MenuItem)
class MenuItemAdmin(admin,ModelAdmin):
    list_display = ('name','price','image')

@admin.register(Restaurant):
list_display = ('name','address')