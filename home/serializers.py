from rest_framework import serializers
from .models import MenuCategory, ContactSubmission, Time, MenuItem     

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']

class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = "__all__"

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

