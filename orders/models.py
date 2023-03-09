from django.db import models
from django.utils import timezone


class Order(models.Model):
    STATUS_CHOICES = [
        ("pedido_realizado", "Pedido Realizado"),
        ("pedido_em_andamento", "Pedido em Andamento"),
        ("entregue", "Entregue"),
    ]

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pedido_realizado"
    )
    buyed_at = models.DateTimeField(default=timezone.now)
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    totalQuantity = models.PositiveIntegerField(default=0)


class OrderedProduct(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="ordered_products"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="ordered_products"
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    buyer = models.IntegerField()