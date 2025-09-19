from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Item , MenuItem
from .serializers import ItemSerializer, MenuItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']):
def menu_items_by_category(request):
    category_name request.Get.get('category')
    if not category_name:
        return Response({"error": "Category parameter is requird"})

    menu_items = MenuItem.objects.filter(category__name__iexact=category_name)

    serializer = MenuItemSerializer(menu_items, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)