from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import order
from .serializers import OrderSerializer

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        orders = Order.objects.filter(user=user).order_by('-created_at')   
        serializer = OrderSerializer(orders, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)       

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