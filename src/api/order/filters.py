import django_filters
from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='total_price', lookup_expr='lte')
    created_at = django_filters.DateFromToRangeFilter()
    is_paid = django_filters.BooleanFilter()
    is_released = django_filters.BooleanFilter()

    class Meta:
        model = Order
        fields = ['status', 'payment_method', 'is_paid', 'is_released', 'created_at']
