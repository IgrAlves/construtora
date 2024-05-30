from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    path = models.ImageField(upload_to="imagens/")
    amount = models.IntegerField(max_length=1000)

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=datetime.now, blank = True)
    itens = models.ManyToManyField(
        Produto,
        through="ItemOrder",
        trough=_fields=("order", "product",)
    )

class 
