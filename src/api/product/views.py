from rest_framework import generics, permissions
from product.models import Product, PromotedProduct
from .serializers import ProductSerializer, PromotedProductSerializer

# ------- PRODUCT CRUD API -------

class ProductListCreateView(generics.ListCreateAPIView):
    """
    GET: Barcha mahsulotlar ro‘yxatini olish
    POST: Yangi mahsulot qo‘shish
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: ID bo‘yicha mahsulotni olish
    PUT/PATCH: ID bo‘yicha mahsulotni tahrirlash
    DELETE: ID bo‘yicha mahsulotni o‘chirish
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ------- PROMOTED PRODUCT CRUD API -------

class PromotedProductListCreateView(generics.ListCreateAPIView):
    """
    GET: Barcha targ‘ib qilingan mahsulotlarni olish
    POST: Yangi targ‘ib mahsulot qo‘shish
    """
    queryset = PromotedProduct.objects.all()
    serializer_class = PromotedProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PromotedProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: ID bo‘yicha targ‘ib mahsulotni olish
    PUT/PATCH: ID bo‘yicha targ‘ib mahsulotni yangilash
    DELETE: ID bo‘yicha targ‘ib mahsulotni o‘chirish
    """
    queryset = PromotedProduct.objects.all()
    serializer_class = PromotedProductSerializer
    permission_classes = [permissions.IsAuthenticated]
