from django.contrib import admin
from src.cart.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    model = Cart


admin.site.register(Cart, CartAdmin)
