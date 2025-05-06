from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailSlugView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),  # GET with filters
    path('user/product/', ProductCreateView.as_view(), name='product-create'),  # POST
    path('user/product/<int:pk>/<slug:slug>/', ProductDetailSlugView.as_view(), name='product-detail-slug'),  # GET, PUT, DELETE
]
