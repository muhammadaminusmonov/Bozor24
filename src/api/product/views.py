from rest_framework import generics, permissions
from product.models import Product
from .serializers import ProductSerializer
from ..permissions import IsOwnerOrReadOnly, IsSeller, IsPlatformAdmin


# GET: Filtered product list
class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        region = self.request.query_params.get('region')

        if category:
            queryset = queryset.filter(category__name=category)
        if region:
            queryset = queryset.filter(region__name=region)
        return queryset


# POST: Create product
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSeller, IsPlatformAdmin]


# GET, PUT, DELETE: Product by pk and slug
class ProductDetailSlugView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSeller, IsPlatformAdmin]
    lookup_field = 'pk'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs['pk'])
