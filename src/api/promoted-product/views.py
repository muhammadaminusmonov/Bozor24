from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from product.models import PromotedProduct
from .serializers import PromotedProductSerializer
from ..permissions import IsSeller, IsPlatformAdmin, IsOwnerOrReadOnly



class UserPromotedProductListCreateView(mixins.ListModelMixin,
                                        mixins.CreateModelMixin,
                                        generics.GenericAPIView):
    serializer_class = PromotedProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return PromotedProduct.objects.none()
        return PromotedProduct.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPromotedProductDetailView(generics.RetrieveAPIView):
    queryset = PromotedProduct.objects.all()
    serializer_class = PromotedProductSerializer
    permission_classes = [IsAuthenticated, IsSeller, IsOwnerOrReadOnly]
    lookup_field = 'pk'



class UserPromotedProductSlugDetailView(generics.RetrieveAPIView):
    queryset = PromotedProduct.objects.all()
    serializer_class = PromotedProductSerializer
    permission_classes = [IsAuthenticated, IsSeller, IsOwnerOrReadOnly]
    lookup_fields = ['pk', 'slug']  # Custom method needed


    def get_object(self):
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        return PromotedProduct.objects.get(pk=pk, product__slug=slug)


# ADMIN VIEWS

class AdminPromotedProductListCreateView(mixins.ListModelMixin,
                                         mixins.CreateModelMixin,
                                         generics.GenericAPIView):
    serializer_class = PromotedProductSerializer
    permission_classes = [IsAuthenticated, IsPlatformAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product__category__name']

    queryset = PromotedProduct.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AdminPromotedProductRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PromotedProduct.objects.all()
    serializer_class = PromotedProductSerializer
    permission_classes = [IsAuthenticated, IsPlatformAdmin]
    lookup_field = 'pk'
