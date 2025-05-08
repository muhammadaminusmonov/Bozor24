from django.urls import path
from .views import (
    UserPromotedProductListCreateView,
    UserPromotedProductDetailView,
    UserPromotedProductSlugDetailView,
    AdminPromotedProductListCreateView,
    AdminPromotedProductRetrieveUpdateView,
)

urlpatterns = [
    # USER
    path('user/promoted-product/', UserPromotedProductListCreateView.as_view(), name='promoted-product-list'),
    path('user/promoted-product/<int:pk>/', UserPromotedProductDetailView.as_view(), name='promoted-product-create'),
    path('user/promoted-product/<int:pk>/<slug:slug>/', UserPromotedProductSlugDetailView.as_view()),

    # ADMIN
    path('admin/promoted-product/', AdminPromotedProductListCreateView.as_view()),
    path('admin/promoted-product/<int:pk>/', AdminPromotedProductRetrieveUpdateView.as_view()),
]
