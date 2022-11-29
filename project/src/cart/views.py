from django.http.response import JsonResponse
from src.product.models import Product
import json
# Create your views here.

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def add_to_cart(request, *args, **kwargs):
    if is_ajax(request):
        body = json.loads(request.body)
        product_id = body.get('product')
        action = body.get('action')
        product = Product.objects.filter(id=product_id)
        if request.user.is_authenticated:
            cart = request.user.user_cart.last()
            cart.update_item(product, action)
            
    return JsonResponse({'status': 'ok'})