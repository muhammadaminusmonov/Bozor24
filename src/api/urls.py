from django.urls import path, include


urlpatterns = [
    path("category/", include("api.category.urls")),
    path("auth/register/", include("api.auth.register.urls")),
    path("auth/login/", include("api.auth.login.urls")),
    path("auth/login_token/", include("api.auth.login_token.urls")),
]