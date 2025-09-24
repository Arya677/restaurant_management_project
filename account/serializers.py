from django.contrib.auth.models import User
from rest_framework import serializers

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            "email": {"required":True},
        }