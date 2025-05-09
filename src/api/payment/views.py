from rest_framework import generics, permissions
from .serializers import PaymentSerializer
from ..permissions import IsOwnerOrReadOnly, IsSeller, IsPlatformAdmin
from django_filters.rest_framework import DjangoFilterBackend

from payment.models import Payment

class User_PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'

    def get_object(self):
        return Payment.objects.get(pk=self.kwargs['pk'])

class Admin_PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    lookup_field = 'pk'

    def get_object(self):
        return Payment.objects.get(pk=self.kwargs['pk'])
