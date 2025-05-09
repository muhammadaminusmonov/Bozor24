import django_filters
from product.models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    region   = django_filters.CharFilter(field_name='region__name', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['category', 'region']
