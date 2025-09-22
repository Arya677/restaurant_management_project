from rest_framework import serializers
from .models import Item, MenuItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class MenuItenSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="categoty.name",read_only=True) 

    class Meta:
        model = MenuItem
        fields = "__all__"   

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must bhi positivr number.")       
  