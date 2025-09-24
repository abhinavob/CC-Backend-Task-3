from rest_framework import serializers
from .models import Item, Order
from django.contrib.auth.models import User

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'quantity', 'price', 'date_created', 'date_restocked']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'quantity', 'price']

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'quantity', 'price']

class ItemRestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'quantity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username'] 

class OrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    item = ItemListSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'item', 'quantity', 'total_price', 'order_date']