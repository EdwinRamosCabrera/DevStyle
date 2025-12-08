from django.db import models
from django.urls import reverse

class Category(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

class Product(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) 
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
