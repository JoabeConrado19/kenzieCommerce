from django.db import models


class ShoppingCarts(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField("products.Product", related_name="shopping_carts")

class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(
        "ShoppingCarts", 
        on_delete=models.CASCADE, 
        related_name="items"
    )
    product = models.ForeignKey(
        "products.Product", 
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)
