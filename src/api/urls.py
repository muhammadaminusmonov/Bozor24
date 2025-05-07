from django.urls import path, include
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('product/', include('api.product.urls')),
    path("category/", include("api.category.urls")),
<<<<<<< HEAD
    path("auth/register/", include("api.auth.register.urls")),
    path("auth/login/", include("api.auth.login.urls")),
    path("auth/login_token/", include("api.auth.login_token.urls")),
    path("auth/logout/", include("api.auth.logout.urls")),
=======
    path("auth/", include("api.auth.urls")),
    path("payment/", include("api.payment.urls")),
    path("cart/", include("api.cart.urls")),
    path("region/", include("api.region.urls")),
>>>>>>> c7c14d0310ec89553a3089625b297ff7aca76daf
]