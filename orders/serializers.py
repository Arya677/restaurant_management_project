from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.Charfield(source="menu_item.name", read_only=True) 
    price = serializers.DecimalField(source="menu_item.price",max_digits=6, decimal_place=2, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
 
  