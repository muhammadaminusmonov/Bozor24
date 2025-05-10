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


from rest_framework.exceptions import NotFound

class TransactionDetailView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return Transaction.objects.get(pk=self.kwargs['pk'])
        except Transaction.DoesNotExist:
            raise NotFound(detail="Transaction not found.")

