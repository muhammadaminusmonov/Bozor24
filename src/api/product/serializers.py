# serializers.py

from rest_framework import serializers
from product.models import Product, ProductImage, PromotedProduct

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    is_promoted = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'price', 'discount', 'discount_limit_date',
            'quantity', 'category', 'region', 'status', 'slug', 'view_count',
            'images', 'is_promoted',
        ]

    def get_is_promoted(self, obj):
        return obj.promotedproduct_set.filter(status=1, view_limit__gt=0).exists()

class PromotedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotedProduct
        fields = ['id', 'product', 'promo_type', 'amount', 'status', 'view_limit']
        read_only_fields = ['status']
