from rest_framework import viewsets, permissions
from comment.models import CommentProduct, CommentUser
from .serializers import CommentProductSerializer, CommentUserSerializer
from ..permissions import IsSeller, IsPlatformAdmin

class CommentProductViewSet(viewsets.ModelViewSet):
    queryset = CommentProduct.objects.all()
    serializer_class = CommentProductSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsSeller | IsPlatformAdmin]
        elif self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        product_id = self.request.query_params.get('product')
        if product_id:
            return self.queryset.filter(product__id=product_id)
        return self.queryset

class CommentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CommentUser.objects.all()
    serializer_class = CommentUserSerializer

    def get_queryset(self):
        seller_id = self.request.query_params.get('seller')
        if seller_id:
            return self.queryset.filter(seller__id=seller_id)
        return self.queryset
