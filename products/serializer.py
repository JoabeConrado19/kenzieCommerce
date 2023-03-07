from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'description', 'price', 'stock', 'available', 'user']
        read_only_fields = ["user"]