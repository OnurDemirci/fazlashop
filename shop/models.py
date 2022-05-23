from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class FavoriteShop(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

