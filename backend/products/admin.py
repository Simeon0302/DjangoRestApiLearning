from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'price']
    
admin.site.register(Product, ProductAdmin)