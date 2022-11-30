from django.urls import path
from src.cart.views import *

app_name = 'cart'
urlpatterns = [
    path('add-to-cart/', view=add_to_cart,name='add-to-cart'),
]
