from django.db.models import Q, F, Case, When, Value, IntegerField
from rest_framework import viewsets, mixins, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from product.models import Product, PromotedProduct
from .serializers import ProductSerializer, PromotedProductSerializer
from api.permissions import IsSeller, IsPlatformAdmin, IsOwnerOrReadOnly
from .filters import ProductFilter

class PublicProductViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    List & Retrieve for storefront; public access.
    """
    queryset = Product.objects.all().select_related('category','region')\
        .prefetch_related('images','promotedproduct_set')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        qs = super().get_queryset()

        # Annotate 1 if active promotion, 0 otherwise
        qs = qs.annotate(
            promoted_flag=Case(
                When(promotedproduct__status=1,
                     promotedproduct__view_limit__gt=0, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('-promoted_flag', '-created_at')

        return qs.distinct()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # bump view_count
        instance.view_count = F('view_count') + 1
        instance.save(update_fields=['view_count'])
        instance.refresh_from_db()

        # decrement view_limit on active promo
        promo = instance.promotedproduct_set.filter(status=1, view_limit__gt=0).first()
        if promo:
            promo.view_limit = F('view_limit') - 1
            if promo.view_limit <= 1:
                promo.status = 2  # mark Inactive
            promo.save(update_fields=['view_limit','status'])

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SellerProductViewSet(viewsets.ModelViewSet):
    """
    Authenticated sellers manage *only* their products.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsSeller, IsPlatformAdmin]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class PromotedProductViewSet(viewsets.ModelViewSet):
    """
    Sellers create/promote; admin can manage any.
    """
    serializer_class = PromotedProductSerializer

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return []
        return [IsSeller() if self.request.user.is_seller else IsPlatformAdmin()]

    def get_queryset(self):
        if self.request.user.is_staff:
            return PromotedProduct.objects.all()
        return PromotedProduct.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status=1)
