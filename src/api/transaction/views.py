# views.py
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from payment.models import Transaction
from .serializers import TransactionSerializer
from api.permissions import IsSeller, IsPlatformAdmin

class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Transaction.objects.all()
        return Transaction.objects.filter(buyer=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)


class TransactionDetailView(generics.RetrieveUpdateAPIView):  # no DestroyAPIView!
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsSeller, IsPlatformAdmin]

    def get_object(self):
        return Transaction.objects.get(pk=self.kwargs['pk'])
