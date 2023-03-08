from rest_framework import serializers
from .models import Order, OrderedProduct


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
