from django.shortcuts import render
from django.db import models
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Order
from . import serializers

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemListSerializer
    permission_classes = [IsAdminUser]

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemCreateSerializer
    permission_classes = [IsAdminUser]

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemUpdateSerializer
    permission_classes = [IsAdminUser]

class ItemRestockView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemRestockSerializer
    permission_classes = [IsAdminUser]

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all().select_related('user', 'item').order_by('-order_date')
    serializer_class = serializers.OrderListSerializer
    permission_classes = [IsAdminUser]

class OrderRevenueView(APIView):
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_revenue = Order.objects.aggregate(total=models.Sum('total_price'))['total']
        return Response({"total_revenue": total_revenue})