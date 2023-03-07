from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'description', 'price', 'stock', 'available', 'user']
