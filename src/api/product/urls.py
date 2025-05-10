from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicProductViewSet, SellerProductViewSet, PromotedProductViewSet

router = DefaultRouter()
router.register(r'products', PublicProductViewSet, basename='public-products')
router.register(r'user/products', SellerProductViewSet, basename='seller-products')
router.register(r'user/promotions', PromotedProductViewSet, basename='seller-promotions')

urlpatterns = [
    path('', include(router.urls)),
]
