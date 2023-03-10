from django.shortcuts import get_object_or_404
from .serializer import OrderSerializer, OrderedProductSerializer
from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from shopping_carts.models import ShoppingCarts
from products.models import Product
from users.models import User
from rest_framework.response import Response


class OrderView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_seller:
            return Order.objects.filter(user=user)
        return Order.objects.none()

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_seller:
            orders = self.get_queryset()
            serializer = self.serializer_class(orders, many=True)
            return Response(serializer.data)
        return Response(
            {"message": "Usuário não autorizado para acessar os pedidos"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class OrderView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_seller or user.is_superuser:
            return Order.objects.filter(user=user)
        return Order.objects.none()

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_seller or user.is_superuser:
            orders = self.get_queryset()
            serializer = self.serializer_class(orders, many=True)
            return Response(serializer.data)
        return Response(
            {"message": "Usuário não autorizado para acessar os pedidos"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def create(self, request, *args, **kwargs):
        user = self.request.user
        queryset = ShoppingCarts.objects.filter(user=user)
        cart = get_object_or_404(queryset)
        sellers = User.objects.filter(is_seller=True)
        total_price = 0
        total_quantity = 0
        for seller in sellers:
            seller_products = Product.objects.filter(user=seller)
            cart_items = cart.items.filter(product__in=seller_products)
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            total_quantity = sum(item.quantity for item in cart_items)
            ordered_products_data = []
            for item in cart_items:
                ordered_products_data.append(
                    {
                        "product": item.product.id,
                        "name": item.product.name,
                        "category": item.product.category,
                        "price": item.product.price,
                        "quantity": item.quantity,
                        "buyer": item.cart.user.id,
                    }
                )
            ordered_products_serializer = OrderedProductSerializer(
                data=ordered_products_data, many=True
            )

            if ordered_products_serializer.is_valid():
                order = Order.objects.create(
                    user=seller,
                    totalPrice=total_price,
                    totalQuantity=total_quantity,
                )
                ordered_products_serializer.save(order=order)
                cart.items.filter(product__in=seller_products).delete()
            else:
                return Response(
                    ordered_products_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response({"message": "Pedidos criados com sucesso"})
