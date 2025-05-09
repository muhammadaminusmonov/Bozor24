from django.urls import path, include

urlpatterns = [
    path('product/', include('api.product.urls')),
    path("category/", include("api.category.urls")),
    path("auth/register/", include("api.auth.register.urls")),
    path("auth/login/", include("api.auth.login.urls")),
    path("auth/login_token/", include("api.auth.login_token.urls")),
    path("auth/logout/", include("api.auth.logout.urls")),
    path("payment/", include("api.payment.urls")),
    path("cart/", include("api.cart.urls")),
    path("review/", include("api.review.urls")),
    path("region/", include("api.region.urls")),
    path("promoted-product/", include("api.promoted-product.urls")),
    path("transaction/", include("api.transaction.urls")),
    path("supportchat/", include("api.supportchat.urls"))
    path("order/", include("api.order.urls")),
    path("comment/", include('api.comment.urls'))
]
