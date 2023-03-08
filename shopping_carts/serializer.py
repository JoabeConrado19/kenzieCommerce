from rest_framework import serializers
from .models import ShoppingCarts, ShoppingCartItem
from products.serializer import ProductSerializer
from products.models import Product


class ShoppingCartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField(default=1, min_value=1)

    class Meta:
        model = ShoppingCartItem
        fields = [
            "id",
            "product",
            "quantity",
        ]

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True, read_only=True)

    def create(self, validated_data: dict) -> ShoppingCarts:
        user = self.context["request"].user
        shopping_cart, created = ShoppingCarts.objects.get_or_create(user=user)
        product_id = self.context["view"].kwargs.get("pk")
        quantity = self.context["request"].query_params.get("quantity", 1)
        cart_item = shopping_cart.items.filter(product__id=product_id).first()

        if cart_item:
            cart_item.quantity += int(quantity)
            cart_item.save()
        else:
            product = Product.objects.get(id=product_id)
            cart_item = ShoppingCartItem.objects.create(
                cart=shopping_cart, 
                product=product, 
                quantity=int(quantity)
            )

        return shopping_cart

    class Meta:
        model = ShoppingCarts
        fields = [
            "id",
            "user",
            "items",
        ]
        read_only_fields = ["user", "items"]

