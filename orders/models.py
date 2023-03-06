from django.db import models


class Order(models.Model):
    order_placed = models.BooleanField(default=True)
    order_in_progress = models.BooleanField(default=False)
    order_delivered = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
