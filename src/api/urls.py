
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('product/', include('api.product.urls')),
    path("category/", include("api.category.urls")),
]