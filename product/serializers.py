from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']

class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    rating = serializers.FloatField(read_only = True)
    category = CategoryShortSerializer(read_only = True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'rating']


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=255)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.FloatField(min_value=0.1)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        if not Category.objects.filter(id=category_id).exists():
            raise ValidationError('"Категория с таким ID не существует!')
        return category_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        from .models import Product
        if not Product.objects.filter(id=product_id).exists():
            raise ValidationError("Продукт с таким ID не существует!")
        return product_id