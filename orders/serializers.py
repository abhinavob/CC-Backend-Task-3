from rest_framework import serializers
from inventory.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'item', 'quantity', 'total_price', 'order_date']