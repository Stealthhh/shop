from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class MyUser(AbstractUser):
    wallet = models.DecimalField(decimal_places=2, max_digits=12, default=1000.00)


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_description = models.TextField(max_length=10000, null=True)
    product_price = models.PositiveIntegerField()
    product_count = models.PositiveIntegerField()


class ObjectBuyProduct(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='user')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='product')
    number_of_product = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class PurchaseReturn(models.Model):
    return_at = models.DateTimeField(auto_now_add=True)
    object_buy_product = models.OneToOneField(ObjectBuyProduct, on_delete=models.DO_NOTHING, related_name='buy_product')