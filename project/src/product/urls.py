from django.urls import path
from src.product.views import ProductListView

urlpatterns = [
    path('', view=ProductListView.as_view()),
]
