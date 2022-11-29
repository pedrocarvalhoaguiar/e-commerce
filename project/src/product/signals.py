from django.db.models.signals import post_save
from src.cart.models import Cart
from src.user.models import CustomUser

def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(owner=instance)

post_save.connect(create_cart, sender=CustomUser)
