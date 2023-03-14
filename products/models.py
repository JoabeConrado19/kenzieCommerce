from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
