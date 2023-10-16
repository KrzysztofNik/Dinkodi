from django.contrib import admin

from .models import Address, ShoppingCart, Transaction

admin.site.register(Address)
admin.site.register(ShoppingCart)
admin.site.register(Transaction)
