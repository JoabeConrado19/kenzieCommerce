from django.db import models


class ShoppingCarts(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
    product = models.ManyToManyField("products.Product", related_name="products")
