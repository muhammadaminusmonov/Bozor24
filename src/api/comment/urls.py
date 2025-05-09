from django.urls import path
from .views import CommentView, CommentDetailView

urlpatterns = [
    path('', CommentView.as_view(), name='comment-list'), 
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail') 
]