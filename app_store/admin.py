from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}   
    ordering = ('code',)
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'stock', 'price', 'category', 'is_available', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    search_fields = ('code', 'name',)
    list_editable = ('stock', 'price', 'category', 'is_available')
    list_per_page = 20


