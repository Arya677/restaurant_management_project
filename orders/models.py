from django.db import models
from .status_models import OrderStatus

class ActiveOrderManager(models.manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',"Pending"),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)                                       
    status = models.ForeignKey(OrderStatus, choices=STATUS_CHOICES, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customere_name}"

 class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_length=5m decimal_places=2)                                            
    created_at = models.DateTimeField(auto_now_Add = True)     

