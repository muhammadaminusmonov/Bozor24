from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from review.models import Review
from .serializers import ReviewSerializers
from ..permissions import IsOwnerOrReadOnly, IsSeller
from review.models import Review


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

# Agar tokken bo'lmasa
    # def perform_create(self, serializer):
    #     # Endi anonim foydalanuvchilar uchun user bo'lmaydi, shuning uchun tekshirish zarur
    #     if self.request.user.is_authenticated:
    #         serializer.save(user=self.request.user)
    #     else:
    #         serializer.save()