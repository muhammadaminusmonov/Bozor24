from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CartSerializer
from cart.models import Cart
from .filters import CartFilter
from ..permissions import IsOwnerOrReadOnly, IsPlatformAdmin, IsSeller

class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartFilter

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Cart.objects.all()
        return Cart.objects.filter(user=user)

class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller, IsPlatformAdmin]
    queryset = Cart.objects.all()
