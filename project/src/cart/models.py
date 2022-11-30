from django.db import models
from src.utility.models import BaseModel
from src.user.models import CustomUser
from src.cart.managers import CartManager
# Create your models here.


class Cart(BaseModel):

    objects = CartManager()

    owner = models.ForeignKey(CustomUser, related_name='user_cart', null=True, on_delete=models.CASCADE)
    
