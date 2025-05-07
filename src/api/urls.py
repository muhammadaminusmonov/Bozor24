from django.urls import path, include


urlpatterns = [
    path("category/", include("api.category.urls")),
    path("auth/", include("api.auth.urls")),
    path("cart/", include("api.cart.urls")),
    path("payment/", include("api.payment.urls")),
]