from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    code = models.TextField()
    street = models.TextField()

class Transaction(models.Model):
    item = models.ForeignKey(Item,related_name='transactions',on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name='transactions')
    address = models.ForeignKey(Address,related_name='transactions',on_delete=models.CASCADE)
    transaction_state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-finished_at',)

class ShoppingCart(models.Model):
    owner = models.ForeignKey(User,related_name='carts',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-added_at',)
