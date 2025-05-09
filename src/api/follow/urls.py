from django.urls import path
from .views import FollowListCreateView, FollowDeleteView

urlpatterns = [
    path('', FollowListCreateView.as_view(), name='follow-list-create'),
    path('<int:pk>/', FollowDeleteView.as_view(), name='follow-delete'),
]
