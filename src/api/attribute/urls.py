from django.urls import path
from attribute.views import AttributeListCreateView, AttributeDetailView

urlpatterns = [
    path('api/admin/attribute/', AttributeListCreateView.as_view(), name='attribute-list-create'),
    path('api/admin/attribute/<int:pk>/', AttributeDetailView.as_view(), name='attribute-detail'),
]
