from django.contrib import admin
from .models import Category, Product, Review

# Регистрация модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

# Регистрация модели Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    list_filter = ['category']
    search_fields = ['title', 'description']
    ordering = ['category']

admin.site.register(Product, ProductAdmin)

# Регистрация модели Review
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'stars', 'text']
    list_filter = ['product', 'stars']
    search_fields = ['text']

admin.site.register(Review, ReviewAdmin)
