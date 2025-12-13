from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class StoreView(ListView):
    template_name = 'store/store.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 4
    