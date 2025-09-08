from django.contrib import admin
from .models import Menu, Order, MenuItem

admin.site.register(Menu)
admin.site.register(Order)

@admin.register(MenuItem)
class MenuItemAdmin(admin,ModelAdmin):
    list_display = ('name','price','image')