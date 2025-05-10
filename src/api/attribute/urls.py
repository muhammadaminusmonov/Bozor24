from django.urls import path
from .views import AttributeListCreateView, AttributeDetailView

urlpatterns = [
    path('', AttributeListCreateView.as_view(), name='attribute-list-create'),
    path('<int:pk>/', AttributeDetailView.as_view(), name='attribute-detail'),
]
