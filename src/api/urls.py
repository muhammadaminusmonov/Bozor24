from django.urls import path, include

urlpatterns = [
    path('product/', include('api.product.urls')),
    path("category/", include("api.category.urls")),
    path("auth/", include("api.auth.urls")),
    path("region/", include("api.region.urls")),
    path("promoted-product/", include("api.promoted-product.urls")),
]
