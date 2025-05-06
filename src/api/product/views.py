from rest_framework import generics, permissions
from product.models import Product
from .serializers import ProductSerializer
from api.permissions import IsSeller, IsOwnerOrReadOnly


# GET: Filtered product list
class ProductListView(generics.ListAPIView):
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
    permission_classes = [permissions.IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# GET, PUT, DELETE: Product by pk and slug
class ProductDetailSlugView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def get_object(self):
        return Product.objects.get(pk=self.kwargs['pk'], slug=self.kwargs['slug'])
