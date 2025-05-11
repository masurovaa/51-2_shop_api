from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', category_list_create_api_view()), #GET, POST
    path('categories/<int:id>/', category_detail_api_view()), #GET, PUT, DELETE
    path('products/', product_list_create_api_view()), #GET, POST
    path('products/<int:id>/', product_detail_api_view()), #GET, PUT, DELETE
    path('products/reviews/', product_reviews_list_api_view()),
    path('reviews/', review_list_create_api_view()), #GET, POST
    path('reviews/<int:id>/', review_detail_api_view()), #GET, PUT, DELETE
    ]