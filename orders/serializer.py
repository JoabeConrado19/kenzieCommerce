from rest_framework import serializers
from .models import Order, OrderedProduct
from rest_framework.exceptions import ValidationError


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = "__all__"
        extra_kwargs = {"order": {"read_only": True}}

    def validate(self, validated_data):
        product = validated_data["product"]
        quantity = validated_data["quantity"]
        if quantity > product.stock:
            raise ValidationError(
                {
                    "message": f"Produto {product.name} com quantidade insuficiente em estoque."
                }
            )
        if not product.available:
            raise ValidationError({"message": f"Produto {product.name} indisponivel."})

        return validated_data


class OrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"
