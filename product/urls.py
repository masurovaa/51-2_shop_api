from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:id>/', CategoryDetailView.as_view()),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('products/reviews/', ProductReviewsListAPIView.as_view()),
    path('reviews/', ReviewListCreateView.as_view()),
    path('reviews/<int:id>/', ReviewDetailView.as_view()),
    path('categories/stats/', CategoryStatsAPIView.as_view()),
]