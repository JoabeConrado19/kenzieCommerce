from django.db import models
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=600)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
