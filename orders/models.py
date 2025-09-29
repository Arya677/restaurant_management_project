from django.db import models
from .status_models import OrderStatus
from .utils import generate_unique_order_id

class ActiveOrderManager(models.manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending','processing'])

class OrderQuerySet(models.QuesrySet):
    def with_status(self, status):
        return self.filetr(status=status)

    def pending(self):
        return self.filter(status='pending')

    def completed(self):
        return self.filter(status='completed')
    
    def cancelled(self):
        return self.filter(status='cancelled')

class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)
    
    def with_status(self,status):
        return self.get_queryset().with_status(status)

    def pending(self):
        return self.get_queryset().completed()
    
    def cancelled(self):
        return self.get_queryset().cancelled()

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
    total_amount = models.CharField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.customere_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.menu_item.name} (Order #{self.order.id})'

    def get_item_total(self):
        return self.menu_item.price * self.quantity

 class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_length=5m decimal_places=2)                                            
    created_at = models.DateTimeField(auto_now_Add = True)     

