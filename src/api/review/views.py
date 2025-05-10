from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from review.models import Review
from .serializers import ReviewSerializers

from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsSeller]
    # Tokken yoq bo'lsa
    # permission_classes = [permissions.AllowAny]


    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to post a review.")
        serializer.save(user=self.request.user)

