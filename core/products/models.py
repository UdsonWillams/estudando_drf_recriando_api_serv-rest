from django.db import models
from accounts.models import User
# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    description = models.CharField(max_length=150, default='Sem descrição')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id}"
