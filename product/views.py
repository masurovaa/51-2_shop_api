from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Product, Review
from .serializers import (CategorySerializer, ProductSerializer,
                          ReviewSerializer, ProductWithReviewsSerializer)
from django.db.models import Avg, Count


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class ProductReviewsListAPIView(APIView):
    def get(self, request):
        products = Product.objects.annotate(rating=Avg('reviews__stars'))
        serializer = ProductWithReviewsSerializer(products, many=True)
        return Response(serializer.data)
    
class CategoryStatsAPIView(APIView):
    def get(self, request):
        categories = Category.objects.annotate(products_count=Count('products'))
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)