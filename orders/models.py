from django.db import models
from .status_models import OrderStatus

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customere_name}"      