
from django.urls import path
from .views import PaymentListCreateView, PaymentDetailView, PaymentCreateView

urlpatterns = [
    path('', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('add/', PaymentCreateView.as_view(), name='payment_add'),  # to‘g‘ri View qo‘shildi
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
]
