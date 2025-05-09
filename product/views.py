from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Category, Product, Review
from .serializers import (CategorySerializer, ProductSerializer,
                          ReviewSerializer, ProductWithReviewsSerializer)
from django.db.models import Avg, Count


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

class ProductReviewsListAPIView(APIView):
    def get(self, request):
        products = Product.objects.annotate(rating=Avg('reviews__stars'))
        serializer = ProductWithReviewsSerializer(products, many=True)
        return Response(serializer.data)
    
class CategoryListAPIViews(APIView):
    def get(self, request):
        categories = Category.objects.annotate(products_count=Count('products'))
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)