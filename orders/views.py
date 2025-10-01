from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModekVeiwSet
from .models import order
from .serializers import OrderSerializer, OrderStatusUpdateSerializer
import random


class OrderHistoryView(APIView):                                                            
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        orders = Order.objects.filter(user=user).order_by('-created_at')   
        serializer = OrderSerializer(orders, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)       

class UpdateOrderStatusView(APIView):
    def put(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)                                              

        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)   
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message':'Order status updated successfully', 'order':serializer.data},
                status = status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

def order_page(request):
    return render(request, "order.html

def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get("customer_name")
        total_amount = request.POST.get('total_amount')

        order = Order.objects.created(
            customer_name = customer_name,
            total_amount=total_amount
        )
        return redirect("order_detail",order_id=order.order_id) 
    return render(request, "orders/create_order.html")  
   
def order_confirmation(request):
    order_number = random.random.randit(1000.99999)
    return render(request, "order_confirmation.html", {"order_number": order_number})

def OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    lookup_field = 'order_id'
    queryset = Order.objects.all()  

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, method=['post'], url_path='cancel')
    def cancel_order(self, request, pk=None):
        try:
            order = self.get_object()
            if order.customer != request.user:
                return Response(
                    {'error':'You are not authorized to cancel this order'},
                    status=status.HTTP_403_FORBIDDEN,
                )
            
            if order.status in ['completed','cancelled']:
                return Response(
                    {'error':f'Order cannot be cancelled, current status: {order.status'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            order.status = 'cancelled'
            order.save()

            return Response(
                {'status':'success','message':'Order has been cancelled.'},
                status=status.HTTP_20_OK,
            )
        except Order.DoesNotExist:
            return Response(
                {'error':'Order not Found.'}, status=status.HTTP_400_NOT_FOUND
            )

