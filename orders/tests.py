from django.test import TestCase
from django.contrib.auth.models import User
from home.models import MenuCategory, MenuItem
from .models import Order, OrderItem
from decimal import decimal

class OrderModelTest(TestCase):
    def setUp(self):
        user USer.objects.create_user(username='testuser', password='testpass')
        category = MenuCategory.objects.create(name='Starters')
        item1 = MenuItem.objects.create(name='Burger',price=Decimal('5.50'),category=category)   
        item2 = MenuItem.objects.create(name='Fries',price=Decimal('2.50'),category=category)

        order = Order.objects.create(customer=user)
        OrderItem.objects.create(order=order, menu_item=item1, quantity=2)
        OrderItem.objects.create(order=order, menu_item=item2, quantity=3)

        self.order = order

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, Decimal('17.00'))                      
