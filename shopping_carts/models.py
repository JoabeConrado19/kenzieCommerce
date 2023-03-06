from django.db import models


class ShoppingCarts(models.Model):
    quantity = models.IntegerField()
    amount_payable = models.DecimalField()
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
    product = models.ManyToManyField("products.Product", related_name="products")
