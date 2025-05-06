from rest_framework import serializers
from product.models import Product, ProductImage, PromotedProduct




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'quantity',
            'category',
            'region',
            'status',
            'slug',
        ]


class PromotedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotedProduct
        fields = '__all__'
