from django.urls import path,include
from .views import ReviewListCreateView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list-create'),
    ]