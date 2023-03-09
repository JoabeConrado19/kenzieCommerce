from .models import ShoppingCarts
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import ShoppingCartSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ShoppingCartsView(ListCreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    queryset = ShoppingCarts.objects.all()
    serializer_class = ShoppingCartSerializer

    def destroy(self, request, *args, **kwargs):
        user = request.user
        shopping_cart = get_object_or_404(ShoppingCarts, user=user)
        product_id = kwargs.get("pk")

        if product_id:
            cart_item = shopping_cart.items.filter(product__id=product_id).first()
            if cart_item:
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    cart_item.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            shopping_cart.items.all().delete()
            shopping_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
