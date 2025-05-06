from django.urls import path, include
from .views import CartListView, CartCreateView, CartDetailView

urlpatterns = [
    path("", CartListView.as_view(), name="cart_list"),
    path("add/", CartCreateView.as_view(), name="cart_create"),
    path("cart/<int:pk>/", CartDetailView.as_view(), name="cart_detail_slug"),
]