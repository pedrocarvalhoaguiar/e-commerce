from django.urls import path
from src.product.views import ProductListView

app_name = 'product'
urlpatterns = [
    path('', view=ProductListView.as_view(), name='home'),
]
