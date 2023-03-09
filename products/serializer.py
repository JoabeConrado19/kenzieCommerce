from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True, source="user")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "category",
            "description",
            "price",
            "stock",
            "available",
            "seller",
        ]
