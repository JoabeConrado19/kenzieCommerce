from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=8, unique=True)
    is_seller = models.BooleanField(default=False, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)
    email = models.EmailField(max_length=127, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
