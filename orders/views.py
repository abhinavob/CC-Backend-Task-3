from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from inventory.models import Order, Item

class PastOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-order_date')

class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        item_id = request.data.get('item')
        quantity = request.data.get('quantity', 1)

        if not item_id:
            return Response({"error": "No item provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        quantity = int(quantity)
        if quantity > item.quantity:
            return Response({"error": f"Not enough stock. {item.quantity} left in stock."}, status=status.HTTP_400_BAD_REQUEST)
        
        total_price = item.price * quantity
        order = Order.objects.create(user=user, item=item, quantity=quantity, total_price=total_price)

        item.quantity -= quantity
        item.save()

        return Response({"order_id": order.id}, status=status.HTTP_201_CREATED)