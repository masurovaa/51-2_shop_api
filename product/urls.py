from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListAPIViews.as_view()),
    path('categories/<int:id>/', CategoryDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('products/reviews/', ProductReviewsListAPIView.as_view()),
    path('reviews/', ReviewListView.as_view()),
    path('reviews/<int:id>/', ReviewDetailView.as_view()),
]