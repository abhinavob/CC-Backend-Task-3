from rest_framework import serializers
from inventory.models import Item

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'price']