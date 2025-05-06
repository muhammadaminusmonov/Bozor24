from django.urls import path, include
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('product/', include('api.product.urls')),
    path("category/", include("api.category.urls")),
    path("auth/", include("api.auth.urls")),
    path("payment/", include("api.payment.urls")),
    path("cart/", include("api.cart.urls")),
    path("region/", include("api.region.urls")),
]