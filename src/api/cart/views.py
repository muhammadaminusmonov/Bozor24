from rest_framework import generics, permissions
from product.models import Product
from .serializers import CartSerializer
from ..permissions import IsOwnerOrReadOnly, IsSeller, IsPlatformAdmin
from cart.models import Cart


class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny]


class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def get_object(self):
        return Cart.objects.get(pk=self.kwargs['pk'])



