from rest_framework import generics, permissions
from supportchat.models import SupportChatRoom, SupportMessage
from .serializers import SupportChatRoomSerializer, SupportMessageSerializer
from ..permissions import IsSeller, IsPlatformAdmin

class SupportChatRoomListCreateView(generics.ListCreateAPIView):
    serializer_class = SupportChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return SupportChatRoom.objects.all()
        return SupportChatRoom.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SupportChatRoomUpdateView(generics.UpdateAPIView):
    queryset = SupportChatRoom.objects.all()
    serializer_class = SupportChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class SupportMessageListCreateView(generics.ListCreateAPIView):
    serializer_class = SupportMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SupportMessage.objects.filter(room_id=self.kwargs['room_id'])

    def perform_create(self, serializer):
        room = SupportChatRoom.objects.get(id=self.kwargs['room_id'])
        serializer.save(sender=self.request.user, room=room)


class SupportMessageUpdateView(generics.UpdateAPIView):
    queryset = SupportMessage.objects.all()
    serializer_class = SupportMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
