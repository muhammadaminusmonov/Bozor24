from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from payment.models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter
from api.permissions import IsPlatformAdmin, IsSeller, IsOwnerOrReadOnly

class PaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsSeller, IsPlatformAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Payment.objects.all()
        return Payment.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsSeller, IsPlatformAdmin]
