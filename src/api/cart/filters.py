import django_filters
from cart.models import Cart

class CartFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Cart
        fields = ['user__username', 'created_at']
