from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from inventory.models import Item
from .serializers import ItemListSerializer

class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()
        price_range = self.request.query_params.get('price')
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        return queryset