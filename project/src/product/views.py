from django.shortcuts import render
from django.views.generic import ListView
from src.product.models import Product
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):

        if self.request.GET.get('q'):
            q = self.request.GET['q']
            queryset = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        else:
            if self.queryset is not None:
                queryset = self.queryset
                if hasattr(queryset, '_clone'):
                    queryset = queryset._clone()
            elif self.model is not None:
                queryset = self.model._default_manager.all()
            else:
                raise ImproperlyConfigured(u"'%s' must define 'queryset' or 'model'"
                                        % self.__class__.__name__)
        return queryset
