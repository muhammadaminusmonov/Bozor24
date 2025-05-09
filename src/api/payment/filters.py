import django_filters
from payment.models import Payment

class PaymentFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')
    method = django_filters.CharFilter()
    amount = django_filters.RangeFilter()
    payment_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Payment
        fields = ['user__username', 'method', 'amount', 'payment_at']
