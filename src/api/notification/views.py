from rest_framework import generics, permissions
from django.core.exceptions import PermissionDenied
from notification.models import Notification
from .serializers import NotificationSerializer
from ..permissions import IsOwnerOrReadOnly, IsSeller, IsPlatformAdmin
from django.core.exceptions import PermissionDenied




class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Tokken yoq bo'lsa
    # permission_classes = [permissions.AllowAny]