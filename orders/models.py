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
        max_length=20, 
        choices=STATUS_CHOICES, 
        default="pedido_realizado"
    )
    buyed_at = models.DateTimeField(default=timezone.now)
    products = models.ManyToManyField("products.Product", through="OrderedProduct")

class OrderedProduct(models.Model):
    order = models.ForeignKey(
        Order, 
        on_delete=models.CASCADE, 
        related_name="ordered_products"
    )
    product = models.ForeignKey(
        "shopping_carts.ShoppingCartItem", 
        on_delete=models.CASCADE, 
        related_name="ordered_products"
    )
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2)
    totalQuantity = models.PositiveIntegerField()
