from django.shortcuts import render
from django.views.generic import TemplateView
from app_store.models import Product, Category

class HomeView(TemplateView):
    template_name = '../../theme/templates/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by('-created_at')[:4]
        context['categories'] = Category.objects.order_by('code')[:3]
        print(context)
        return context
    


