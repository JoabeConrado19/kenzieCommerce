from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    number = models.IntegerField()

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
