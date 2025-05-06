from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    PromotedProductListCreateView, PromotedProductDetailView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('promoted/', PromotedProductListCreateView.as_view(), name='promoted-list-create'),
    path('promoted/<int:pk>/', PromotedProductDetailView.as_view(), name='promoted-detail'),
]
