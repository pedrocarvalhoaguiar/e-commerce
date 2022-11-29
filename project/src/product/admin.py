from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'id', )


admin.site.register(Product, ProductAdmin)
