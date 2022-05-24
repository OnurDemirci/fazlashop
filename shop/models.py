from email.mime import image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to="shops")
    def __str__(self):
        return self.name


class FavoriteShop(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to="products")
    def __str__(self):
        return self.name


class FavoriteProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

