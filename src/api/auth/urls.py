from django.urls import path, include

urlpatterns = [
    path("register/", include("api.auth.register.urls")),
    path("login/", include("api.auth.login.urls")),
    path("login_token/", include("api.auth.login_token.urls")),
]