from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','description','images',]