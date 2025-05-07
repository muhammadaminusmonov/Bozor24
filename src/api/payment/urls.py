from django.urls import path, include
from .views import User_PaymentListView, Admin_PaymentListView

urlpatterns = [
    path('user/', User_PaymentListView.as_view(), name='payment_list'),
    path('user/<int:pk>/',User_PaymentListView.as_view(), name='payment_list_pk'),
    path('admin/', Admin_PaymentListView.as_view(), name='payment_create'),
    path('admin/<int:pk>/', Admin_PaymentListView.as_view(), name='payment_detail'),
]