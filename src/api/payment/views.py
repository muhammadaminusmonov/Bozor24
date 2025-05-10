from django.core.exceptions import PermissionDenied
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from payment.models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter
from api.permissions import IsPlatformAdmin, IsSeller, IsOwnerOrReadOnly

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Faqat login bo‘lgan foydalanuvchilar
    # permission_classes = [IsSeller, IsPlatformAdmin]  # Faqat seller va admin
    # permission_classes = [permissions.AllowAny]  # Faqat login bo‘lgan foydalanuvchilar
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Faqat login bo‘lgan foydalanuvchilar
    # permission_classes = [permissions.AllowAny]  # Faqat login bo‘lgan foydalanuvchilar

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            serializer.save(user=None)




class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        user = self.request.user
        return Payment.objects.all()