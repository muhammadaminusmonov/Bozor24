from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentProductViewSet, CommentUserViewSet

router = DefaultRouter()
router.register(r'comments/product', CommentProductViewSet, basename='commentproduct')
router.register(r'comments/user', CommentUserViewSet, basename='commentuser')

urlpatterns = [
    path('', include(router.urls)),
]
