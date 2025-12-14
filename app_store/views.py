from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category

class StoreView(ListView):
    template_name = 'store/store.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9   

    def get_queryset(self):
        category_slug = self.request.GET.get('category')
        queryset = super().get_queryset()
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.request.GET.get('category')
        context['categories'] = Category.objects.all()
        context['category_selected'] = category_slug
        return context


