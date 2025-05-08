from rest_framework import serializers
from product.models import PromotedProduct

class PromotedProductSerializer(serializers.ModelSerializer):
    promo_type_display = serializers.CharField(source='get_promo_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    product_title = serializers.CharField(source='product.title', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PromotedProduct
        fields = '__all__'
        read_only_fields = ['user']  # user field is auto set in view
