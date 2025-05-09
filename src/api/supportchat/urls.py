from django.urls import path
from .views import (
    SupportChatRoomListCreateView,
    SupportChatRoomUpdateView,
    SupportMessageListCreateView,
    SupportMessageUpdateView,
)

urlpatterns = [
    path('support-rooms/', SupportChatRoomListCreateView.as_view(), name='support-room-list-create'),
    path('support-rooms/<int:pk>/update/', SupportChatRoomUpdateView.as_view(), name='support-room-update'),
    path('support-rooms/<int:room_id>/messages/', SupportMessageListCreateView.as_view(), name='support-message-list-create'),
    path('support-messages/<int:pk>/update/', SupportMessageUpdateView.as_view(), name='support-message-update'),
]
