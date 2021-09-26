from products.models import Products
from django.db import models
from accounts.models import User


# Create your models here.
class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    products = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f" Carrinho de {self.user}"
